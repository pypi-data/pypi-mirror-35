import concurrent.futures

from flask import current_app


__all__ = ('Executor', )
__version__ = '0.3.0'


class Executor:

    def __init__(self, app=None):
        self.app = app
        self._executor = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('EXECUTOR_TYPE', 'thread')
        app.config.setdefault('EXECUTOR_MAX_WORKERS', None)
        self._executor = self._make_executor(app)
        app.extensions['executor'] = self

    def _make_executor(self, app):
        executor_type = app.config['EXECUTOR_TYPE']
        executor_max_workers = app.config['EXECUTOR_MAX_WORKERS']
        if executor_type == 'thread':
            _executor = concurrent.futures.ThreadPoolExecutor
        elif executor_type == 'process':
            _executor = concurrent.futures.ProcessPoolExecutor
        else:
            raise ValueError("{} is not a valid executor type.".format(executor_type))
        return _executor(max_workers=executor_max_workers)

    def submit(self, fn, *args, **kwargs):
        if type(self._executor) == concurrent.futures.ThreadPoolExecutor:
            fn = with_app_context(fn, current_app._get_current_object())
        return self._executor.submit(fn, *args, **kwargs)

    def job(self, fn):
        if type(self._executor) == concurrent.futures.ProcessPoolExecutor:
            raise TypeError("Can't decorate {}: Executors that use multiprocessing"
                            " don't support decorators".format(fn))
        return ExecutorJob(executor=self, fn=fn)


class ExecutorJob:

    def __init__(self, executor, fn):
        self.executor = executor
        self.fn = fn

    def submit(self, *args, **kwargs):
        future = self.executor.submit(self.fn, *args, **kwargs)
        return future


def with_app_context(fn, app):
    def wrapper(*args, **kwargs):
        with app.app_context():
            return fn(*args, **kwargs)
    return wrapper
