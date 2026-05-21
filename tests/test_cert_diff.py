import datetime
from src.diff.cert_diff import CertRenewalDiff
from src.core.models import CertificateInfo

def test_renewal_detection():
    now = datetime.datetime.now(datetime.timezone.utc)
    c1 = CertificateInfo("a", 443, "a", [], "CA", now, now + datetime.timedelta(days=10), 10, "TLSv1.3", "C", "sn1")
    c2 = CertificateInfo("a", 443, "a", [], "CA", now, now + datetime.timedelta(days=90), 90, "TLSv1.3", "C", "sn2")
    assert CertRenewalDiff.is_renewed(c1, c2) is True
