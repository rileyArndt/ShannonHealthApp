import hashlib as hash
from datetime import date


username = input("Email Address>:") #accepts users email
while '@' not in username or '.' not in username:
    print("Please enter valid email")
    username = input("Email Address>:") #accepts users email upon failure
sal = str(date.today()) # keep this to generate a salt and pass as encrypted data
secret = hash.md5((sal + input("Password >:")).encode())   #placeholder

print(username + '\n' + sal + '\n' + secret.hexdigest())

