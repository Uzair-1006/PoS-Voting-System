from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import binascii

def verify_signature(public_key_pem: str, data: str, signature_hex: str) -> bool:
    try:
        public_key = RSA.import_key(public_key_pem)
        hashed_data = SHA256.new(data.encode('utf-8'))
        signature = binascii.unhexlify(signature_hex)
        pkcs1_15.new(public_key).verify(hashed_data, signature)
        return True
    except Exception:
        return False
