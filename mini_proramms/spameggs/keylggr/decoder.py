import rsa

pubkey, privkey = rsa.newkeys(512)

str1 = ('HELLO MY DEAR FRIEND')

enctex = rsa.encrypt(str1.encode(), pubkey)

dectex = rsa.decrypt(enctex, privkey).decode()
print("The primordial string: ", str1)
print("The Encrypted message: ", enctex)
print("The Decrypted message: ", dectex)