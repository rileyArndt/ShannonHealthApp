
# Adding all the modules
from mods import *
from str_builder import *
from Perscription import perscreen
from Chatbot import chatresponses, chatai, dataextraction
from main import *
import mysql.connector
from mysql.connector import Error
import hashlib as hash
import hashlib as hash
from datetime import date
import mysql.connector
from mysql.connector import Error
import geocoder
import socket
import datetime
import hashlib as hash
from datetime import date
import mysql.connector
from mysql.connector import Error
import geocoder
import socket
import datetime

dbpass= os.environ.get('dbpass')
mailpass= os.environ.get('mailpass')




def create(self):


    connection = mysql.connector.connect(host = "shannontestdatabase.cxc8luynmyvm.us-east-1.rds.amazonaws.com",
    user = "admin",
    passwd =  dbpass)
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

    name1 = str(self.root.get_screen("create").ids.mail1.text)
    name2 = str(self.root.get_screen("create").ids.mail2.text)
    while '@' not in name1 or '.' not in name1:
        self.root.get_screen("create").ids.warning_label.text = "please enter a valid email"
        return
    if name1 != name2:
        self.root.get_screen("create").ids.warning_label.text = "emails do not match"
    elif 1 <= grabQuery("select count(*) from auth where email='" + name1 + "';")[0][0]:
        self.root.get_screen("create").ids.warning_label.text = "an account under this email already exists"
    else:
        self.root.current = "create2"

def create2(self):

    connection = mysql.connector.connect(host = "shannontestdatabase.cxc8luynmyvm.us-east-1.rds.amazonaws.com",
    user = "admin",
    passwd =  dbpass)
    print("Connection initialized")
    cursor = connection.cursor()
    cursor.execute("use shannon;")

    def insertQuery(query):
        try:
            cursor.execute(query)
            connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")

    name1 = str(self.root.get_screen("create").ids.mail1.text)
    name2 = str(self.root.get_screen("create").ids.mail2.text)
    if name1 != name2:
        self.root.get_screen("create").ids.warning_label.text = "passwords do not match"
    else:
        sal = str(date.today()) # keep this to generate a salt and pass as encrypted data
        secret = hash.md5((sal + str(self.root.get_screen("create2").ids.mail2.text)).encode())   #placeholder
        hashbrown = secret.hexdigest()
        ip = geocoder.ip("me")
        city = ip.city
        realip = socket.gethostbyname(socket.gethostname())
        time = str(datetime.datetime.now())[:-7]
        insertQuery("""insert into auth (email, phash, sal, logintime, location, ip)
        values ('""" + name1 + "', '" +hashbrown + "', '" + 
        sal + "', '" +time + "', '" + city + "', '" + realip + "');") 
        self.root.current = "login"       ###CHANGE TO LANGING PAGE




def forgot(self):
    import smtplib
    import yagmail
    import random
    from random import randint
    random.seed() 
    global seed
    seed = randint(111111,999999)
    #try:
    #    ygm = yagmail.SMTP('smtp.gmail.com', 587)
    #    # smtp.ehlo()
    #    ygm.starttls()
    #    ygm.login("noreply.prototypeapp@gmail.com",mailpass)

    #    subject = "Your vertification code"
    #    body = seed

    #    msg = f'Subject: {subject}\n\n{body}'

    #    ygm.send("noreply.prototypeapp@gmail.com", self.root.get_screen("forgot").ids.mail1.text, msg)
    #except:
    #    print("debug: failed to send email to " + self.root.get_screen("forgot").ids.mail1.text)
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login("noreply.prototypeapp@gmail.com",mailpass)

            subject = "Your vertification code"
            body = seed

            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail("noreply.prototypeapp@gmail.com", self.root.get_screen("forgot").ids.mail1.text, msg)
        self.root.current = "forgot2"
    except:
        print("debug: failed to send email to " + self.root.get_screen("forgot").ids.mail1.text)
        
def forgot2(self):
    if self.root.get_screen("forgot2").ids.mail1.text == str(seed):
        self.root.current = "forgot3"
    else:
        self.root.get_screen("forgot2").ids.warning_label.text = "Invalid Code"

def forgot3(self):


    connection = mysql.connector.connect(host = "shannontestdatabase.cxc8luynmyvm.us-east-1.rds.amazonaws.com",
    user = "admin",
    passwd =  dbpass)
    print("Connection initialized")
    cursor = connection.cursor()
    cursor.execute("use shannon;")

    def insertQuery(query):
        try:
            cursor.execute(query)
            connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")
        
    def grabQuery(query):
        connection = None 
        try:
            cursor.execute(query)
            ret = cursor.fetchall()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")
        return ret

    
    name1 = str(self.root.get_screen("forgot3").ids.mail1.text)
    name2 = str(self.root.get_screen("forgot3").ids.mail2.text)

    if name1 == name2:
        sal = grabQuery(""" 
        select sal from auth 
        where email = '""" + self.root.get_screen("forgot").ids.mail1.text +"';")
        sal = sal[0][0]
        secret = hash.md5((sal +str(self.root.get_screen("forgot3").ids.mail2.text)).encode())   
        secret = secret.hexdigest()
        insertQuery("update auth set phash = '" + secret + "' where email = '"+ self.root.get_screen("forgot").ids.mail1.text +"';")
    else:
        self.root.get_screen("forgot3").ids.warning_label.text = "Passwords do not match"

