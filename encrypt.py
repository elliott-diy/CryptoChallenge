import builtins
import os
os.urandom = lambda n: (_ for _ in ()).throw(NotImplementedError("Legacy system."))
import random
import time
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
FLAG = b"FLAG{example_flag}"


random.seed()

key_material = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(16))
print("[DEBUG] Key material:", key_material)

key = hashlib.sha256(key_material.encode()).digest()

cipher = AES.new(key, AES.MODE_CBC, iv=b'\x00' * 16)
ciphertext = cipher.encrypt(pad(FLAG, 16))

try:
    hex_flag = ciphertext.encode("hex")
except AttributeError:
    hex_flag = ciphertext.hex()

print("[DEBUG] Encrypted flag (hex):", hex_flag)
print("[DEBUG] Time used (int):", int(time.time()))
