from src.guard import SSLExpiryGuard

def test_guard_scan():
    guard = SSLExpiryGuard()
    res = guard.scan_host("example.com")
    assert res["status"] == "HEALTHY"
    assert res["security_grade"] == "STRONG"
    assert res["cert"].hostname == "example.com"
