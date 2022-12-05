from Crypto.Cipher import Blowfish
from struct import pack

bs = Blowfish.block_size
key = b'Um mundo melhor'
ciphertext = b""
print(type(ciphertext))
iv = ciphertext[:bs]
ciphertext = ciphertext[bs:]
cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
msg = cipher.decrypt(ciphertext)
last_byte = msg[-1]
msg = msg[:- (last_byte if type(last_byte) is int else ord(last_byte))]
print(msg)