import json
from typing import Dict, Any

class SlackAlertNotifier:
    @staticmethod
    def build_payload(hostname: str, days: int, severity: str) -> Dict[str, Any]:
        emoji = ":rotating_light:" if severity == "CRITICAL" else ":warning:"
        return {
            "text": f"{emoji} SSL Alert: *{hostname}* expires in {days} days!"
        }
