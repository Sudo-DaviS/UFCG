from Crypto.Cipher import Blowfish
from struct import pack
bs = Blowfish.block_size
key = b'Um mundo melhor'
cipher = Blowfish.new(key, Blowfish.MODE_CBC)
txt = str(input())
texto = bytes(txt, 'utf-8')
plaintext = texto
plen = bs - len(plaintext) % bs
padding = [plen]*plen
padding = pack('b'*plen, *padding)
msg = cipher.iv + cipher.encrypt(plaintext +paddin)
with open('ciphertext.txt', 'w') as arquivo:
 print(msg, file=arquivo)
print(msg)
#pycryptodome.com