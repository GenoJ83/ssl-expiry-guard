from src.ocsp.staple import check_ocsp_staple

def test_ocsp():
    assert check_ocsp_staple(True) == "STAPLED"
    assert check_ocsp_staple(False) == "NOT_STAPLED"
