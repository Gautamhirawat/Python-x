import unittest
from encryption.encryption import encrypt, generate_key

class TestEncryption(unittest.TestCase):

    def test_encryption(self):
        data = "Hello, World!"
        password = b"mysecretpassword"
        key = generate_key(password)
        encrypted_data = encrypt(data, key)
        self.assertNotEqual(data, encrypted_data)
        self.assertIsInstance(encrypted_data, bytes)

if __name__ == "__main__":
    unittest.main()
