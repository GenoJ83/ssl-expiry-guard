from src.notify.slack import SlackAlertNotifier

def test_slack_alert():
    p = SlackAlertNotifier.build_payload("mycorp.com", 3, "CRITICAL")
    assert "mycorp.com" in p["text"]
    assert ":rotating_light:" in p["text"]
