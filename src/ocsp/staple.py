def check_ocsp_staple(has_staple: bool) -> str:
    return "STAPLED" if has_staple else "NOT_STAPLED"
