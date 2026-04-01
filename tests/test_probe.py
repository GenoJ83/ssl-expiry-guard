from src.probe.simulator import MockTLSProber

def test_mock_prober():
    prober = MockTLSProber(days_until_expiry=30)
    info = prober.probe("api.github.com")
    assert info.hostname == "api.github.com"
    assert info.days_remaining == 30
    assert info.tls_version == "TLSv1.3"
