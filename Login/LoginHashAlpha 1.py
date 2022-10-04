import hashlib as hash
from datetime import date
import mysql.connector
from mysql.connector import Error

def sqlSession(query):
    connection = None
    try: 
        connection = mysql.connector.connect(host = "shannontestdatabase.cxc8luynmyvm.us-east-1.rds.amazonaws.com",
        user = "admin",
        passwd = input("password>:"))
        print("Connection initialized")
        passQuery(connection, query)
    except Error as err:
        print(f"Error: '{err}'")

def passQuery (connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        #connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

username = input("Email Address>:") #accepts users email
while '@' not in username or '.' not in username:
    print("Please enter valid email")
    username = input("Email Address>:") #accepts users email upon failure
sal = str(date.today()) # keep this to generate a salt and pass as encrypted data
secret = hash.md5((sal + input("Password >:")).encode())   #placeholder
sdate = sqlSession(""" 
use shannon;
select sal
from auth where email = 'ndiazdelopediaz@angelo.edu';
""")

print(username + '\n' + sal + '\n' + secret.hexdigest())

