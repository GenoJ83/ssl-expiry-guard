from src.san.matcher import hostname_matches_san

def test_san_matching():
    sans = ["example.com", "*.example.com", "sub.*.io"]
    assert hostname_matches_san("example.com", sans) is True
    assert hostname_matches_san("api.example.com", sans) is True
    assert hostname_matches_san("other.org", sans) is False
