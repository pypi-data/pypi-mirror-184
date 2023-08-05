from azure.core.settings import settings
from azure.core.tracing.ext.opentelemetry_span import OpenTelemetrySpan
from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

TRACING_IS_CONFIGURED = False


def configure_tracing():
    global TRACING_IS_CONFIGURED
    if TRACING_IS_CONFIGURED:
        # tracing should only be set up once
        # to avoid duplicated trace handling.
        # global variables is the pattern used
        # by opentelemetry, so we use the same
        return

    # declare OTEL as enabled tracing plugin for Azure SDKs
    settings.tracing_implementation = OpenTelemetrySpan

    # setup OTEL tracing
    trace.set_tracer_provider(TracerProvider())

    # setup azure monitor trace exporter to send telemetry to appinsights
    # no need to set conn str, as default is appinsights anyways
    trace_exporter = AzureMonitorTraceExporter()
    span_processor = BatchSpanProcessor(trace_exporter)
    trace.get_tracer_provider().add_span_processor(span_processor)

    # setup console span exporter
    # trace_exporter = ConsoleSpanExporter()
    # span_processor = BatchSpanProcessor(trace_exporter)
    # trace.get_tracer_provider().add_span_processor(span_processor)

    TRACING_IS_CONFIGURED = True


def get_tracer(name: str):
    tracer = trace.get_tracer(name)
    return tracer
