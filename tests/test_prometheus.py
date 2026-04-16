from src.export.prometheus import PrometheusExporter
from src.guard import SSLExpiryGuard

def test_prometheus_export():
    guard = SSLExpiryGuard()
    metrics = PrometheusExporter.to_metrics(guard.scan_fleet(["app.io"]))
    assert "ssl_cert_days_remaining" in metrics
    assert 'host="app.io"' in metrics
