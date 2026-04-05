import datetime
from src.alert.rules import ExpiryAlertRule
from src.core.models import CertificateInfo

def test_alert_rules():
    rule = ExpiryAlertRule(warning_threshold_days=30, critical_threshold_days=7)
    now = datetime.datetime.now(datetime.timezone.utc)
    
    c_crit = CertificateInfo("crit.com", 443, "crit.com", [], "CA", now, now, 5, "TLSv1.3", "CIPHER", "1")
    assert rule.evaluate(c_crit)["severity"] == "CRITICAL"
    
    c_warn = CertificateInfo("warn.com", 443, "warn.com", [], "CA", now, now, 20, "TLSv1.3", "CIPHER", "2")
    assert rule.evaluate(c_warn)["severity"] == "WARNING"
    
    c_ok = CertificateInfo("ok.com", 443, "ok.com", [], "CA", now, now, 60, "TLSv1.3", "CIPHER", "3")
    assert rule.evaluate(c_ok) is None
