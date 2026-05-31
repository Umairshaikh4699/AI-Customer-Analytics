from Crypto.PublicKey import ECC
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

def generate_ecc_keypair(curve="P-256"):
    key = ECC.generate(curve=curve)
    priv_pem = key.export_key(format='PEM')
    pub_pem = key.public_key().export_key(format='PEM')
    return priv_pem, pub_pem

def ecc_encrypt(recipient_pub_pem: bytes, plaintext: bytes, aad: bytes=b""):
    eph = ECC.generate(curve="P-256")
    recipient_pub = ECC.import_key(recipient_pub_pem)
    
    # Derives the shared secret point (Ephemeral Public Key * Recipient Private Key)
    # The result of multiplication is a point Q (shared_point)
    shared_point = recipient_pub.pointQ * eph.d 
    
    # Extract the X-coordinate of the shared point (sx) and convert it to bytes
    # This is the ECC shared secret used as the input to the KDF
    sx = int(shared_point.x).to_bytes((shared_point.x.size_in_bits() + 7) // 8, 'big')
    
    # Derive the 32-byte (256-bit) AES key using HKDF (Hash-based Key Derivation Function)
    key = HKDF(sx, 32, b"", SHA256)
    
    nonce = get_random_bytes(12)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    
    if aad:
        cipher.update(aad)
        
    ct, tag = cipher.encrypt_and_digest(plaintext)
    
    eph_pub_pem = eph.public_key().export_key(format='PEM')
    return eph_pub_pem, nonce, ct, tag

def ecc_decrypt(recipient_priv_pem: bytes, eph_pub_pem: bytes, nonce: bytes, ciphertext: bytes, tag: bytes, aad: bytes = b""):
    recipient_priv = ECC.import_key(recipient_priv_pem)
    eph_pub = ECC.import_key(eph_pub_pem)
    
    # Derives the shared secret point (Ephemeral Public Key * Recipient Private Key)
    # This is the same shared point calculated in ecc_encrypt
    shared_point = eph_pub.pointQ * recipient_priv.d
    
    # Extract the X-coordinate of the shared point (sx) and convert it to bytes
    sx = int(shared_point.x).to_bytes((shared_point.x.size_in_bits() + 7) // 8, 'big')
    
    # Derive the 32-byte (256-bit) AES key using HKDF
    key = HKDF(sx, 32, b"", SHA256)
    
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    
    if aad:
        cipher.update(aad)
        
    pt = cipher.decrypt_and_verify(ciphertext, tag)
    
    return pt

if __name__ == "__main__":
    priv, pub = generate_ecc_keypair("P-256")
    msg = b"Hello ECC hybrid!"
    
    eph_pub, nonce, ct, tag = ecc_encrypt(pub, msg)
    
    plain = ecc_decrypt(priv, eph_pub, nonce, ct, tag)
    print("decrypted:", plain)