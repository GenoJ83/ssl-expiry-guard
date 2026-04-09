from src.reporter.table import TerminalReport
from src.guard import SSLExpiryGuard

def test_table_report():
    guard = SSLExpiryGuard()
    results = guard.scan_fleet(["host1.com", "host2.com"])
    txt = TerminalReport.render(results)
    assert "HOSTNAME" in txt
    assert "host1.com" in txt
