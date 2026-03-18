import datetime
from src.parser.cert_parser import CertParser

def test_days_remaining():
    now = datetime.datetime(2026, 4, 1, tzinfo=datetime.timezone.utc)
    expiry = datetime.datetime(2026, 4, 21, tzinfo=datetime.timezone.utc)
    assert CertParser.calculate_days_remaining(expiry, now=now) == 20
    past = datetime.datetime(2026, 3, 1, tzinfo=datetime.timezone.utc)
    assert CertParser.calculate_days_remaining(past, now=now) == 0
    
def test_san_parsing():
    sans = [("DNS", "example.com"), ("DNS", "*.example.com"), ("IP", "1.1.1.1")]
    assert CertParser.parse_san(sans) == ["example.com", "*.example.com"]
