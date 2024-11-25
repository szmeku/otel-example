# OpenTelemetry Collector Demo

```shell
docker compose up -d
```

The demo exposes the following backends:
- Jaeger at http://0.0.0.0:16686  Distributed tracing visualization - shows request flows across services
- Zipkin at http://0.0.0.0:9411  Alternative trace viewer with different UI/features
- Prometheus at http://0.0.0.0:9090 Time-series metrics visualization and querying

Dummy traces
```bash
curl -X POST http://localhost:4318/v1/traces -H "Content-Type: application/json" -d "{\"resourceSpans\":[{\"resource\":{\"attributes\":[{\"key\":\"service.name\",\"value\":{\"stringValue\":\"curl-test\"}},{\"key\":\"environment\",\"value\":{\"stringValue\":\"test\"}}]},\"scopeSpans\":[{\"spans\":[{\"name\":\"process-order\",\"kind\":1,\"startTimeUnixNano\":\"$(date +%s%N)\",\"endTimeUnixNano\":\"$(date +%s%N)\",\"traceId\":\"$(openssl rand -hex 16)\",\"spanId\":\"$(openssl rand -hex 8)\",\"attributes\":[{\"key\":\"http.method\",\"value\":{\"stringValue\":\"POST\"}},{\"key\":\"http.url\",\"value\":{\"stringValue\":\"/api/orders\"}},{\"key\":\"http.status_code\",\"value\":{\"intValue\":200}}]}]}]}]}"
```

Dummy metrics
```bash
curl -X POST http://localhost:4318/v1/metrics -H "Content-Type: application/json" -d '{"resourceMetrics":[{"resource":{"attributes":[{"key":"service.name","value":{"stringValue":"curl-test"}}]},"scopeMetrics":[{"metrics":[{"name":"test_counter","sum":{"dataPoints":[{"asDouble":1.0,"timeUnixNano":"'$(date +%s%N)'"}]}}]}]}]}' 
```

Dummy logs
# logs push
```bash
    curl -X POST http://localhost:4318/v1/logs -H "Content-Type: application/json" -d '{"resourceLogs":[{"resource":{"attributes":[{"key":"service.name","value":{"stringValue":"curl-test"}}]},"scopeLogs":[{"logRecords":[{"timeUnixNano":"'$(date +%s%N)'","severityText":"INFO","body":{"stringValue":"Test log message"}}]}]}]}'
```
