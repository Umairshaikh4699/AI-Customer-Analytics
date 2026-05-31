from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def generate_rsa_keypair(bits=2048):
    key = RSA.generate(bits)
    private_pem = key.export_key()
    public_pem = key.publickey().export_key()
    return private_pem, public_pem

def rsa_encrypt(public_pem: bytes, plaintext: bytes):
    pub = RSA.import_key(public_pem)
    cipher = PKCS1_OAEP.new(pub)  # uses SHA-1 by default, can configure
    return cipher.encrypt(plaintext)

def rsa_decrypt(private_pem: bytes, ciphertext: bytes):
    priv = RSA.import_key(private_pem)
    cipher = PKCS1_OAEP.new(priv)
    return cipher.decrypt(ciphertext)

def rsa_sign(private_pem: bytes, message: bytes):
    priv = RSA.import_key(private_pem)
    h = SHA256.new(message)
    signature = pkcs1_15.new(priv).sign(h)
    return signature

def rsa_verify(public_pem: bytes, message: bytes, signature: bytes):
    pub = RSA.import_key(public_pem)
    h = SHA256.new(message)
    try:
        pkcs1_15.new(pub).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

if __name__ == "__main__":
    priv, pub = generate_rsa_keypair(2048)
    message = b"Secret via RSA"
    ciphertext = rsa_encrypt(pub, message)
    print("ciphertext:", ciphertext.hex())

    decrypted = rsa_decrypt(priv, ciphertext)
    print("decrypted:", decrypted)

    sig = rsa_sign(priv, message)

    print("signature valid?", rsa_verify(pub, message, sig))