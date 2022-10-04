import hashlib as hash
from datetime import date
import mysql.connector
from mysql.connector import Error
import geocoder
import socket
import datetime

connection = mysql.connector.connect(host = "shannontestdatabase.cxc8luynmyvm.us-east-1.rds.amazonaws.com",
user = "admin",
passwd =  input("Database password>:"))
print("Connection initialized")
cursor = connection.cursor()
cursor.execute("use shannon;")

def grabQuery(query):
    connection = None 

    try:
        cursor.execute(query)
        ret = cursor.fetchall()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
    return ret


def insertQuery(query):
   
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

good = False
while good == False:
    username = input("Email Address>:") #accepts users email
    while '@' not in username or '.' not in username:
        print("Please enter valid email")
        username = input("Email Address>:") #accepts users email upon failure
    secret = input("Password >:")

    sal = grabQuery(""" 
    select sal from auth 
    where email = '""" + username +"';")
    if len(sal) > 0:
        sal = sal[0][0]
        good = True
        secret = hash.md5((sal + secret).encode())   #placeholder
        secret = secret.hexdigest()
        if secret == grabQuery("select phash from auth where email='" + username + "';")[0][0]: 
            city = geocoder.ip("me").city
            realip = socket.gethostbyname(socket.gethostname())
            time = str(datetime.datetime.now())[:-7]
            insertQuery("update auth set location = '" + city + "', ip = '" + realip+"', logintime = '" + time + "' where email = '"+ username+ "';")
            print("Account Authorized")
        else:
            good = False
            print("Could not authenticate user, please re-enter your credentials.")
    else:
        print("Could not authenticate user, please re-enter your credentials.")


print(username + '\n' + sal + '\n' + secret)

