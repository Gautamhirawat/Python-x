import unittest
from encryption.encryption import encrypt, generate_key
from encryption.decryption import decrypt

class TestDecryption(unittest.TestCase):

    def test_decryption(self):
        data = "Hello, World!"
        password = b"mysecretpassword"
        key = generate_key(password)
        encrypted_data = encrypt(data, key)
        decrypted_data = decrypt(encrypted_data, key)
        self.assertEqual(data, decrypted_data)

if __name__ == "__main__":
    unittest.main()

