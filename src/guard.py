from typing import List, Dict, Any
from src.core.models import CertificateInfo
from src.probe.simulator import MockTLSProber
from src.alert.rules import ExpiryAlertRule
from src.cipher.evaluator import CipherEvaluator

class SSLExpiryGuard:
    def __init__(self, warning_days: int = 30, critical_days: int = 7, prober=None):
        self.rule = ExpiryAlertRule(warning_days, critical_days)
        self.prober = prober or MockTLSProber()
        
    def scan_host(self, hostname: str, port: int = 443) -> Dict[str, Any]:
        cert = self.prober.probe(hostname, port)
        alert = self.rule.evaluate(cert)
        grade, reason = CipherEvaluator.evaluate(cert.tls_version, cert.cipher_suite)
        return {
            "cert": cert,
            "alert": alert,
            "security_grade": grade,
            "security_reason": reason,
            "status": "HEALTHY" if not alert else alert["severity"]
        }
        
    def scan_fleet(self, hostnames: List[str]) -> List[Dict[str, Any]]:
        return [self.scan_host(h) for h in hostnames]
