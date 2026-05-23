import json
from typing import List, Dict, Any

def export_json(scan_results: List[Dict[str, Any]]) -> str:
    items = []
    for r in scan_results:
        c = r["cert"]
        items.append({
            "hostname": c.hostname,
            "port": c.port,
            "days_remaining": c.days_remaining,
            "status": r["status"],
            "tls_version": c.tls_version,
            "issuer": c.issuer
        })
    return json.dumps(items, indent=2)
