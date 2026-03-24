from src.cipher.evaluator import CipherEvaluator

def test_cipher_evaluation():
    grade, reason = CipherEvaluator.evaluate("TLSv1.3", "TLS_AES_256_GCM_SHA384")
    assert grade == "STRONG"
    
    grade_old, _ = CipherEvaluator.evaluate("TLSv1.0", "AES128-SHA")
    assert grade_old == "INSECURE"
    
    grade_weak, _ = CipherEvaluator.evaluate("TLSv1.2", "ECDHE-RSA-RC4-SHA")
    assert grade_weak == "WEAK"
