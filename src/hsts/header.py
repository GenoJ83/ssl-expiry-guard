def check_hsts_header(hsts_header: str) -> bool:
    return "max-age=" in hsts_header.lower()
