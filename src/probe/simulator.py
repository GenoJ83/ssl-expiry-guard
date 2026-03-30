import datetime
from typing import Dict, Any
from src.core.models import CertificateInfo
from src.parser.cert_parser import CertParser

class MockTLSProber:
    def __init__(self, days_until_expiry: int = 45, tls_version: str = "TLSv1.3"):
        self.days_until_expiry = days_until_expiry
        self.tls_version = tls_version
        
    def probe(self, hostname: str, port: int = 443) -> CertificateInfo:
        now = datetime.datetime.now(datetime.timezone.utc)
        valid_from = now - datetime.timedelta(days=45)
        valid_until = now + datetime.timedelta(days=self.days_until_expiry)
        return CertificateInfo(
            hostname=hostname,
            port=port,
            subject_cn=hostname,
            san_list=[hostname, f"*.{hostname}"],
            issuer="Let's Encrypt Authority R3",
            valid_from=valid_from,
            valid_until=valid_until,
            days_remaining=self.days_until_expiry,
            tls_version=self.tls_version,
            cipher_suite="TLS_AES_256_GCM_SHA384",
            serial_number="04a8b7c9d1e2f3"
        )
