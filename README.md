# OpenTelemetry Collector Demo

```shell
docker compose up -d
```

The demo exposes the following backends:

- Jaeger at http://0.0.0.0:16686
- Zipkin at http://0.0.0.0:9411
- Prometheus at http://0.0.0.0:9090

Run this to feed collector with dummy trace
```bash
curl -X POST http://localhost:4318/v1/traces -H "Content-Type: application/json" -d "{\"resourceSpans\":[{\"resource\":{\"attributes\":[{\"key\":\"service.name\",\"value\":{\"stringValue\":\"curl-test\"}},{\"key\":\"environment\",\"value\":{\"stringValue\":\"test\"}}]},\"scopeSpans\":[{\"spans\":[{\"name\":\"process-order\",\"kind\":1,\"startTimeUnixNano\":\"$(date +%s%N)\",\"endTimeUnixNano\":\"$(date +%s%N)\",\"traceId\":\"$(openssl rand -hex 16)\",\"spanId\":\"$(openssl rand -hex 8)\",\"attributes\":[{\"key\":\"http.method\",\"value\":{\"stringValue\":\"POST\"}},{\"key\":\"http.url\",\"value\":{\"stringValue\":\"/api/orders\"}},{\"key\":\"http.status_code\",\"value\":{\"intValue\":200}}]}]}]}]}"
```
