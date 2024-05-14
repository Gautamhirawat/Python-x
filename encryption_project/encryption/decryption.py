from cryptography.fernet import Fernet

def decrypt(data: bytes, key: bytes) -> str:
    """Decrypt the provided data with the provided key."""
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(data).decode()
    return decrypted_data

