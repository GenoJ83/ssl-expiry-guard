import fnmatch
from typing import List

def hostname_matches_san(hostname: str, san_patterns: List[str]) -> bool:
    for pat in san_patterns:
        if fnmatch.fnmatch(hostname.lower(), pat.lower()):
            return True
    return False
