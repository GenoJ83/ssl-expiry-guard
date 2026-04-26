import argparse

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="sslguard", description="TLS certificate expiry guard")
    p.add_argument("--version", action="store_true", help="Print version")
    p.add_argument("hosts", nargs="*", default=["example.com"], help="Hostnames to scan")
    p.add_argument("--warn-days", type=int, default=30, help="Warning threshold")
    p.add_argument("--crit-days", type=int, default=7, help="Critical threshold")
    return p

def main(args=None):
    p = build_parser()
    opts = p.parse_args(args)
    if opts.version:
        print("sslguard v0.1.0")
        return 0
    return 0
