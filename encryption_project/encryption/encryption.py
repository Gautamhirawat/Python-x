from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(password: bytes) -> bytes:
    """Generate a key from a given password."""
    # Derive a 32-byte key from the password using SHA-256
    derived_key = hashlib.sha256(password).digest()
    # Base64 encode the key to make it compatible with Fernet
    return base64.urlsafe_b64encode(derived_key)

def encrypt(data: str, key: bytes) -> bytes:
    """Encrypt the provided data with the provided key."""
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

