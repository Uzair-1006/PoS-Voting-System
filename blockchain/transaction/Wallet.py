from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import binascii

class Wallet:
    def __init__(self):
        self._private_key = RSA.generate(1024)
        self._public_key = self._private_key.publickey()

    def sign(self, data: str) -> str:
        """Sign the data string using SHA256 + RSA private key"""
        hashed_data = SHA256.new(data.encode('utf-8'))
        signature = pkcs1_15.new(self._private_key).sign(hashed_data)
        return binascii.hexlify(signature).decode('utf-8')

    def public_key_string(self) -> str:
        """Return the public key in PEM format as a string"""
        return self._public_key.export_key().decode('utf-8')

    def save_keys(self, private_path: str, public_path: str):
        """Save private and public keys to .pem files"""
        with open(private_path, 'wb') as f:
            f.write(self._private_key.export_key())
        with open(public_path, 'wb') as f:
            f.write(self._public_key.export_key())

    def from_key(self, filepath: str):
        """Load a private key from a .pem file"""
        with open(filepath, 'rb') as f:
            self._private_key = RSA.import_key(f.read())
            self._public_key = self._private_key.publickey()
