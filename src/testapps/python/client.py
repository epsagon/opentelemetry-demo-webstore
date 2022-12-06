import asyncio
import aiohttp
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import Resource
from opentelemetry.instrumentation.aiohttp_client import (
    AioHttpClientInstrumentor
)

AioHttpClientInstrumentor().instrument()

provider = TracerProvider(resource=Resource.create({'test.aiohttp': 'hio'}))
exporter = OTLPSpanExporter(endpoint="http://0.0.0.0:4318/v1/traces")
processor = BatchSpanProcessor(span_exporter=exporter)
trace.set_tracer_provider(provider)
provider.add_span_processor(processor)
