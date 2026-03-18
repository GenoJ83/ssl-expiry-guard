import datetime
from typing import Tuple, List, Dict, Any

class CertParser:
    @staticmethod
    def calculate_days_remaining(valid_until: datetime.datetime, now: datetime.datetime = None) -> int:
        now = now or datetime.datetime.now(datetime.timezone.utc)
        delta = valid_until - now
        return max(0, delta.days)
        
    @staticmethod
    def parse_san(san_tuples: List[Tuple[str, str]]) -> List[str]:
        return [val for kind, val in san_tuples if kind.lower() == "dns"]
