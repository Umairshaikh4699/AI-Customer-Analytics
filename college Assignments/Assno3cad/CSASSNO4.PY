from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA256

# BLOCK_SIZE 16 # Not strictly needed for AES-GCM as the block size is fixed at 16 bytes for AES

def aes_gcm_encrypt(key: bytes, plaintext: bytes, aad: bytes=b""):
    nonce = get_random_bytes(12)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    if aad:
        cipher.update(aad)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    return nonce, ciphertext, tag

def aes_gcm_decrypt(key: bytes, nonce: bytes, ciphertext: bytes, tag: bytes, aad: bytes=b""):
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    if aad:
        cipher.update(aad)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext

if __name__ == "__main__":
    key = get_random_bytes(32)
    message = b"Hello-AES-GCM encrypt test"
    aad = b"header-or-associated-data"

    nonce, ct, tag = aes_gcm_encrypt(key, message, aad)
    print("nonce:", nonce.hex())
    print("ciphertext:", ct.hex())
    print("tag:", tag.hex())

    pt = aes_gcm_decrypt(key, nonce, ct, tag, aad)
    print("decrypted:", pt)