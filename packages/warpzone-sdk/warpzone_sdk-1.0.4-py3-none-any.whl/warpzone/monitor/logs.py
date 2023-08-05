# NOTE: OpenTelemetry logging to Azure is still in EXPERIMENTAL mode!
import logging

from azure.monitor.opentelemetry.exporter import AzureMonitorLogExporter
from opentelemetry.sdk import _logs as logs
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor

LOGGING_IS_CONFIGURED = False


def configure_logging():
    global LOGGING_IS_CONFIGURED
    if LOGGING_IS_CONFIGURED:
        # logging should only be set up once
        # to avoid duplicated log handling.
        # global variables is the pattern used
        # by opentelemetry, so we use the same
        return

    # setup OTEL logging
    logs.set_logger_provider(LoggerProvider())

    # setup azure monitor log exporter to send telemetry to appinsights logging.
    # no need to set conn str, as default is appinsights anyways
    log_exporter = AzureMonitorLogExporter()
    log_record_processor = BatchLogRecordProcessor(log_exporter)
    logs.get_logger_provider().add_log_record_processor(log_record_processor)

    # setup console log exporter
    # log_exporter = ConsoleLogExporter()
    # log_record_processor = BatchLogRecordProcessor(log_exporter)
    # logs.get_logger_provider().add_log_record_processor(log_record_processor)

    LOGGING_IS_CONFIGURED = True


def get_logger(name: str):
    # set up standard logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.hasHandlers():
        # add OTEL handler
        otel_handler = LoggingHandler()
        logger.addHandler(otel_handler)

    return logger
