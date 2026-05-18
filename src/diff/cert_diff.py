from typing import Dict, Any
from src.core.models import CertificateInfo

class CertRenewalDiff:
    @staticmethod
    def is_renewed(old_cert: CertificateInfo, new_cert: CertificateInfo) -> bool:
        return new_cert.serial_number != old_cert.serial_number and new_cert.valid_until > old_cert.valid_until
