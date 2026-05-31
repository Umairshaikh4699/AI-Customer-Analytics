from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def des_encrypt(key: bytes, plaintext: bytes):
    # key must be 8 bytes
    cipher = DES.new(key, DES.MODE_CBC)
    iv = cipher.iv
    ct = cipher.encrypt(pad(plaintext, DES.block_size))
    return iv, ct

def des_decrypt(key: bytes, iv: bytes, ciphertext: bytes):
    cipher = DES.new(key, DES.MODE_CBC, iv=iv)
    pt = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return pt

if __name__ == "__main__":
    key = b"8bytekey"  # Exactly 8 bytes
    message = b"DES demo message, insecure!"

    iv, ct = des_encrypt(key, message)

    print("iv:", iv.hex())
    print("ct:", ct.hex())
    print("decrypted:", des_decrypt(key, iv, ct))