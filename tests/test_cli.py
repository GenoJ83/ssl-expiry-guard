from src.cli.main import build_parser, main

def test_cli():
    p = build_parser()
    opts = p.parse_args(["google.com", "--warn-days", "45"])
    assert opts.hosts == ["google.com"]
    assert opts.warn_days == 45
    assert main(["--version"]) == 0
