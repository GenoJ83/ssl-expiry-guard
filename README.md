# ssl-expiry-guard

Automated TLS/SSL certificate lifecycle monitor, cipher suite auditor, SNI handshake validator, and expiration alerting engine.

[![CI](https://github.com/GenoJ83/ssl-expiry-guard/actions/workflows/ci.yml/badge.svg)](https://github.com/GenoJ83/ssl-expiry-guard/actions)

## Features
- **Automated Lifecycle Alerts**: Configurable tiered thresholds (Warning, Critical)
- **Cipher Suite & Protocol Audit**: Flags deprecated SSLv3, TLS 1.0, TLS 1.1, and weak ciphers
- **Prometheus Metrics Exporter**: Native `ssl_cert_days_remaining` gauge metrics
- **Fleet Scan**: Audit entire fleets of hostnames concurrently

## Quick Start
```python
from src.guard import SSLExpiryGuard

guard = SSLExpiryGuard(warning_days=30, critical_days=7)
res = guard.scan_host('example.com')
print(f"Expires in: {res['cert'].days_remaining} days, Status: {res['status']}")
```
