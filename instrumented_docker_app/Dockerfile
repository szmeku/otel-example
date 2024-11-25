FROM python:3.9-slim

WORKDIR /app

RUN pip install opentelemetry-distro \
    opentelemetry-exporter-otlp \
    opentelemetry-instrumentation-logging \
    flask

RUN opentelemetry-bootstrap -a install

COPY . .

CMD ["opentelemetry-instrument", "--traces_exporter", "otlp", "--metrics_exporter", "otlp", "--logs_exporter", "otlp", "python", "app.py"]