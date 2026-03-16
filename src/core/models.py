from dataclasses import dataclass, field
from typing import List, Optional
import datetime

@dataclass
class CertificateInfo:
    hostname: str
    port: int
    subject_cn: str
    san_list: List[str]
    issuer: str
    valid_from: datetime.datetime
    valid_until: datetime.datetime
    days_remaining: int
    tls_version: str
    cipher_suite: str
    serial_number: str
