from src.ca.known_ca import is_well_known_ca

def test_ca_recognition():
    assert is_well_known_ca("Let's Encrypt Authority R3") is True
    assert is_well_known_ca("Self-Signed Untrusted Root") is False
