import logging
import functools

import google.cloud.logging
from google.cloud.logging.resource import Resource
from opencensus.trace import tracer as tracer_module
from opencensus.trace import execution_context
from opencensus.trace.exporters import stackdriver_exporter
from opencensus.trace.exporters.transports import background_thread
from opencensus.trace.tracers.noop_tracer import NoopTracer
from opencensus.trace.samplers.probability import ProbabilitySampler


testing = False


class LogFactory():
    @classmethod
    def instance(cls):
        if testing is True:
            return DummyInstances()
        else:
            return GCloudInstances()


class Singleton(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '__instance'):
            cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)

        return cls.__instance


class GCloudInstances(metaclass=Singleton):
    def __init__(self):
        self._log_client = google.cloud.logging.Client()
        self._log_client.setup_logging(log_level=logging.INFO)

        self._exporter = stackdriver_exporter.StackdriverExporter(
            transport=background_thread.BackgroundThreadTransport)

    def logger(self, name):
        if hasattr(self, '_log_client'):
            return self._log_client.logger(name)
        else:
            return None

    def tracer(self):
        if hasattr(self, '_exporter'):
            return tracer_module.Tracer(exporter=self._exporter,
                                        sampler=ProbabilitySampler(rate=0.1))
        else:
            return tracer_module.Tracer()


class DummyInstances(metaclass=Singleton):
    class DummyLogger():
        def log_struct(self, *args, **kwargs):
            pass

        def log_text(self, *args, **kwargs):
            pass

    def logger(self, name):
        return DummyInstances.DummyLogger()

    def tracer(self):
        return tracer_module.Tracer()


def info(label, data):
    """Write log to StackDriver.

    data should be dictionary type.
    """
    logger = LogFactory.instance().logger(name=label)

    LOG_RESOURCE = Resource(type='container', labels={})
    try:
        logger.log_struct(info=data,
                          severity='INFO',
                          resource=LOG_RESOURCE)
    except Exception as e:
        logger.log_text(text=data.__str__(),
                        severity='ERROR',
                        resource=LOG_RESOURCE)


def warn(label, data):
    logger = LogFactory.instance().logger(name=label)

    LOG_RESOURCE = Resource(type='container', labels={})
    try:
        logger.log_struct(info=data,
                          severity='WARNING',
                          resource=LOG_RESOURCE)
    except Exception as e:
        logger.log_text(text=data.__str__(),
                        severity='ERROR',
                        resource=LOG_RESOURCE)


def report():
    pass


def trace_entry():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            tracer = execution_context.get_opencensus_tracer()

            if type(tracer) is NoopTracer:
                tracer = LogFactory.instance().tracer()
                tracer.store_tracer()

            with tracer.span(name=func.__name__):
                ret_val = func(*args, **kwargs)

            tracer.finish()
            execution_context.set_opencensus_tracer(NoopTracer())

            return ret_val
        return wrapper
    return decorator


def trace_subcall():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            tracer = execution_context.get_opencensus_tracer()

            with tracer.span(name=func.__name__):
                ret_val = func(*args, **kwargs)

            return ret_val
        return wrapper
    return decorator
