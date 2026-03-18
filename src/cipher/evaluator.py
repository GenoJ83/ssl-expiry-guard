from typing import Tuple

WEAK_CIPHERS = ["RC4", "DES", "3DES", "MD5", "NULL", "EXPORT"]
SECURE_PROTOCOLS = ["TLSv1.2", "TLSv1.3"]

class CipherEvaluator:
    @staticmethod
    def evaluate(tls_version: str, cipher_suite: str) -> Tuple[str, str]:
        if tls_version not in SECURE_PROTOCOLS:
            return "INSECURE", f"Deprecated protocol: {tls_version}"
        for weak in WEAK_CIPHERS:
            if weak in cipher_suite.upper():
                return "WEAK", f"Weak cipher component: {weak}"
        return "STRONG", "Modern cipher and protocol negotiation"
