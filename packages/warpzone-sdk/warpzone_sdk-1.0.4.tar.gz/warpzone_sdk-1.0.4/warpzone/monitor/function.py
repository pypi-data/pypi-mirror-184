from . import logs, traces


def configure_monitoring():
    traces.configure_tracing()
    logs.configure_logging()
