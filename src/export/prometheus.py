from typing import List, Dict, Any

class PrometheusExporter:
    @staticmethod
    def to_metrics(scan_results: List[Dict[str, Any]]) -> str:
        lines = ["# HELP ssl_cert_days_remaining Days remaining until certificate expiration",
                 "# TYPE ssl_cert_days_remaining gauge"]
        for r in scan_results:
            c = r["cert"]
            lines.append(f'ssl_cert_days_remaining{{host="{c.hostname}",port="{c.port}"}} {c.days_remaining}')
        return "\n".join(lines)
