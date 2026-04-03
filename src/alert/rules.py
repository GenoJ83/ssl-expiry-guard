from typing import Optional, Dict, Any
from src.core.models import CertificateInfo

class ExpiryAlertRule:
    def __init__(self, warning_threshold_days: int = 30, critical_threshold_days: int = 7):
        self.warning_days = warning_threshold_days
        self.critical_days = critical_threshold_days
        
    def evaluate(self, cert: CertificateInfo) -> Optional[Dict[str, Any]]:
        if cert.days_remaining <= self.critical_days:
            return {
                "severity": "CRITICAL",
                "days": cert.days_remaining,
                "message": f"Certificate for {cert.hostname} expires in {cert.days_remaining} days!"
            }
        elif cert.days_remaining <= self.warning_days:
            return {
                "severity": "WARNING",
                "days": cert.days_remaining,
                "message": f"Certificate for {cert.hostname} expires soon: {cert.days_remaining} days remaining."
            }
        return None
