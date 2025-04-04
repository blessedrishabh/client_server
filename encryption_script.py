from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES3

class AesEncryption():
    def __init__(self):
        self.key = b"this_is_a_secret"  # AES key size can be 16, 24, or 32 bytes
        self.iv = get_random_bytes(16)  # AES block size is 16 bytes
        self.cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
    def encrypt(self, plaintext):
        # Ensure the plaintext is a multiple of the block size
        padded_data = pad(plaintext.encode(), AES.block_size)
        ciphertext = self.cipher.encrypt(padded_data)
        return ciphertext
    def decrypt(self, ciphertext):
        # Create a new cipher object for decryption with the same key and IV
        cipher_decrypt = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypted_data = unpad(cipher_decrypt.decrypt(ciphertext), AES.block_size)
        return decrypted_data.decode()
    
class CeasarCipher():
    def __init__(self, shift):
        self.shift = shift % 26  # Ensure the shift is within the range of 0-25

    def encrypt(self, plaintext):
        encrypted = ""
        for char in plaintext:
            if char.isalpha():
                base = ord('a') if char.islower() else ord('A')
                encrypted += chr((ord(char) - base + self.shift) % 26 + base)
            else:
                encrypted += char
        return encrypted

    def decrypt(self, ciphertext):
        decrypted = ""
        for char in ciphertext:
            if char.isalpha():
                base = ord('a') if char.islower() else ord('A')
                decrypted += chr((ord(char) - base - self.shift) % 26 + base)
            else:
                decrypted += char
        return decrypted
class Des3Encryption():
    def __init__(self, key):
        self.key = key
        self.cipher = DES3.new(self.key, DES3.MODE_ECB)

    def encrypt(self, plaintext):
        padded_data = pad(plaintext.encode(), DES3.block_size)
        ciphertext = self.cipher.encrypt(padded_data)
        return ciphertext

    def decrypt(self, ciphertext):
        decrypted_data = unpad(self.cipher.decrypt(ciphertext), DES3.block_size)
        return decrypted_data.decode()
    
# ae = AesEncryption()
# encrypted = ae.encrypt("Rishabh")
# print("Encrypted:", encrypted)
# decrypted = ae.decrypt(encrypted)
# print("Decrypted:", decrypted)
# print("\n\n")
# ce = CeasarCipher(5)
# encrypted = ce.encrypt("Rishabh")
# print("Encrypted:", encrypted)
# decrypted = ce.decrypt(encrypted)
# print("Decrypted:", decrypted)
# print("\n\n")
# de = Des3Encryption(b'12345678abcdefgh')
# encrypted = de.encrypt("Rishabh")
# print("Encrypted:", encrypted)
# decrypted = de.decrypt(encrypted)
# print("Decrypted:", decrypted)
