from typing import List, Dict, Any

class TerminalReport:
    @staticmethod
    def render(scan_results: List[Dict[str, Any]]) -> str:
        h1 = "HOSTNAME"
        h2 = "EXPIRES IN"
        h3 = "GRADE"
        h4 = "STATUS"
        lines = [f"{h1:<25} | {h2:<12} | {h3:<10} | {h4}"]
        lines.append("-" * 65)
        for r in scan_results:
            cert = r["cert"]
            status = r["status"]
            grade = r["security_grade"]
            lines.append(f"{cert.hostname:<25} | {str(cert.days_remaining) + 'd':<12} | {grade:<10} | {status}")
        return "\n".join(lines)
