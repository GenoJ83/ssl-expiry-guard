class SSLExpiryError(Exception):
    """Base exception."""

class HandshakeTimeoutError(SSLExpiryError):
    """Raised when TLS handshake times out."""

class CertificateExpiredError(SSLExpiryError):
    """Raised when certificate has already expired."""
