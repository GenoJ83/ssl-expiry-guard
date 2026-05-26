from src.hsts.header import check_hsts_header

def test_hsts():
    assert check_hsts_header("max-age=31536000; includeSubDomains") is True
    assert check_hsts_header("none") is False
