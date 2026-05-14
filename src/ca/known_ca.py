KNOWN_CAS = ["Let's Encrypt", "DigiCert", "Sectigo", "Google Trust Services", "Amazon"]

def is_well_known_ca(issuer: str) -> bool:
    return any(ca.lower() in issuer.lower() for ca in KNOWN_CAS)
