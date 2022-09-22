import hashlib as hash
from datetime import date


username = input("Username>:")
sal = str(date.today()) # keep this to generate a salt and pass as encrypted data (not final)
secret = hash.md5((sal + input("Password >:")).encode())

print(username + '\n' + sal + '\n' + secret.hexdigest())


#need to generate a session key here


#vertify with server
