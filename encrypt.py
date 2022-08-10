import os
from cryptography.fernet import Fernet

files = []
sure = False

for file in os.listdir():
    if file == 'thekey.key':
        
        sure = True
        break
    
inp = 'y'    
if sure:
    inp = 'n'
    inp = str(input('Documents alredy encrypted, want to do this again ? you will lose all your files becouse they will be double incripted and you will lost the first key! if you realy want to double encrypt, make sure you will sava the first key \n want to double encrypt ?(y/n)\n'))
    
if inp == 'y':
    for file in os.listdir():
        if file == 'encrypt.py' or file == '.gitattributes' or file == 'README.md' or file == 'decrypt.py':
            continue
        if file != "thekey.key":
            if os.path.isfile(file):
                files.append(file)

    key = Fernet.generate_key()

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
