from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
from termcolor import colored

key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

print(colored(f"This is the private_key: {private_key}", "green"))
print(colored(f"This is the public_key: {public_key}", "green"))

message = b"Johnson Is Awesome"
cipher_key = PKCS1_OAEP.new(RSA.import_key(public_key))
cipher_text = cipher_key.encrypt(message)
print(colored(f"Encrypted message is: {cipher_text}", "green"))

cipher_key = PKCS1_OAEP.new(RSA.import_key(private_key))
plain_text = cipher_key.decrypt(cipher_text)
print(colored(f"Decrypted message is: {plain_text.decode()}", "green"))
