import json
from src.export.json_out import export_json
from src.guard import SSLExpiryGuard

def test_json_fleet_export():
    guard = SSLExpiryGuard()
    data = json.loads(export_json(guard.scan_fleet(["test.org"])))
    assert len(data) == 1
    assert data[0]["hostname"] == "test.org"
