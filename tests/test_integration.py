from src.guard import SSLExpiryGuard
from src.reporter.table import TerminalReport
from src.export.prometheus import PrometheusExporter

def test_full_ssl_guard_lifecycle():
    guard = SSLExpiryGuard()
    fleet = guard.scan_fleet(["api.github.com", "cdn.example.org"])
    assert len(fleet) == 2
    report = TerminalReport.render(fleet)
    assert "api.github.com" in report
    prom = PrometheusExporter.to_metrics(fleet)
    assert "ssl_cert_days_remaining" in prom
