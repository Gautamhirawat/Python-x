from encryption.encryption import encrypt, generate_key
from encryption.decryption import decrypt

# Example usage
data = "Hello, World!"
password = b"mysecretpassword"

key = generate_key(password)
encrypted_data = encrypt(data, key)
decrypted_data = decrypt(encrypted_data, key)

print(f"Encrypted: {encrypted_data}")
print(f"Decrypted: {decrypted_data}")

# Encrypting and decrypting user input
user_data = input("Enter the text to encrypt: ")
user_password = input("Enter your password: ").encode()

user_key = generate_key(user_password)
user_encrypted_data = encrypt(user_data, user_key)
print(f"Encrypted: {user_encrypted_data}")

user_decrypted_data = decrypt(user_encrypted_data, user_key)
print(f"Decrypted: {user_decrypted_data}")
