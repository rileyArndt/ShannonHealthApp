import hashlib as hash
from datetime import date
import datetime
import mysql.connector
from mysql.connector import Error
import geocoder
import socket


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


passq = False
while passq == False:
    username = input("Email Address>:") #accepts users email
    while '@' not in username or '.' not in username:
        print("Please enter valid email")
        username = input("Email Address>:") #accepts users email upon failure
    hold = grabQuery(""" 
    select email
    from auth where email = '""" + username + "';")
    if len(hold) == 0:
        passq = True
    if passq == True:
        print("Connection inizialized message. \nDevelopers note: Create and pass data through kivy to central manager")
    else:
        print("Account already exists please enter new credentials.")

sal = str(date.today()) # keep this to generate a salt and pass as encrypted data
secret = hash.md5((sal + input("Password >:")).encode())   #placeholder
hashbrown = secret.hexdigest()
ip = geocoder.ip("me")
city = ip.city
realip = socket.gethostbyname(socket.gethostname())
time = str(datetime.datetime.now())[:-7]
if passq == True:
    insertQuery("""insert into auth (email, phash, sal, logintime, location, ip)
    values ('""" + username + "', '" +hashbrown + "', '" + 
    sal + "', '" +time + "', '" + city + "', '" + realip + "');") 

