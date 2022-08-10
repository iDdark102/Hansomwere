import os
from cryptography.fernet import Fernet

files = []

#print(os.listdir())

for file in os.listdir():
    if file == 'valdemort.py':
        continue
    if file != "thekey.key":
        if os.path.isfile(file):
            if file == 'ola.txt' or file == 'img.jpg':
                files.append(file)

key = Fernet.generate_key()

with open("thekey.key", 'rb') as key:
    secretkey = key.read()
    

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)