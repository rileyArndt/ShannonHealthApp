# Mitchell Martin
# 10/11/2022


# Adding all the modules
from matplotlib.patches import Rectangle
from matplotlib.ticker import MaxNLocator
from numpy import full
from mods import *
from str_builder import *
from Perscription import perscreen
from Chatbot import chatresponses, chatai, dataextraction



class Login (Screen):
    pass
# The MainScreen class's functionality is on kivy. 
#
# Let me know if you
# only want to make a screen using python.
class MainScreen(Screen):
   pass

class Create (Screen):
    pass

class Create2(Screen):
    pass

class Forgot (Screen):
    pass

class Forgot2 (Screen):
    pass

class Forgot3 (Screen):
    pass




class CustomOneLineIconListItem(OneLineIconListItem):
   icon = StringProperty()

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      
   def print_item(self, instance):
      self.cartdb = mysql.connector.connect(
         host = "localhost",
         user = "test_user",
         passwd = "pass",
         database = "testing_features"
      )
      self.c2 = self.cartdb.cursor()
      
      query = "INSERT INTO cart SELECT id, product_name, price FROM products WHERE id = '" + instance.text[:6] + "'"
      print(query)
      self.c2.execute(query)
      
      self.cartdb.commit()
   

# Add all your created screens
# to the screen manager.
global sm
sm = ScreenManager()
sm.add_widget(Login(name='login'))
sm.add_widget(MainScreen(name='main'))



# Builds the application.
class MainApp(MDApp):
   def build(self):

      screen = Builder.load_string(complete_app_builder)
      return screen  
   
   def switch_mode(self):
      self.theme_cls.theme_style = (
         "Dark" if self.theme_cls.theme_style == "Light" else "Light"
      )
      pass
   
   def get_out(self):
      exit(0)
      
    
   def logger(self):
      import hashlib as hash
      from datetime import date
      import mysql.connector
      from mysql.connector import Error
      import geocoder
      import socket
      import datetime

      
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

      def insertQuery(query):
          try:
              cursor.execute(query)
              connection.commit()
              print("Query successful")
          except Error as err:
              print(f"Error: '{err}'")


      username = str(self.root.get_screen("login").ids.user.text)
      while '@' not in username or '.' not in username:
          self.root.get_screen("login").ids.warning_label.text = "please enter a valid email"
          return
      secret = str(self.root.get_screen("login").ids.password.text)
      sal = grabQuery(""" 
      select sal from auth 
      where email = '""" + username +"';")
      if len(sal) > 0:
          sal = sal[0][0]
          secret = hash.md5((sal + secret).encode())   #placeholder
          secret = secret.hexdigest()
          if secret == grabQuery("select phash from auth where email='" + username + "';")[0][0]: 
              city = geocoder.ip("me").city
              realip = socket.gethostbyname(socket.gethostname())
              time = str(datetime.datetime.now())[:-7]
              insertQuery("update auth set location = '" + city + "', ip = '" + realip+"', logintime = '" + time + "' where email = '"+ username+ "';")
              sm.current = 'menu'
          else:
              self.root.get_screen("login").ids.warning_label.text = "Could not authenticate user, please re-enter your credentials."
              return
      else:
          self.root.get_screen("login").ids.warning_label.text = "Could not authenticate user, please re-enter your credentials."
          return


   def create(self):
       import hashlib as hash
       from datetime import date
       import mysql.connector
       from mysql.connector import Error

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
       import hashlib as hash
       from datetime import date
       import mysql.connector
       from mysql.connector import Error
       import geocoder
       import socket
       import datetime

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
       import random
       from random import randint
       random.seed() 
       global seed
       seed = randint(111111,999999)
       with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
           smtp.ehlo()
           smtp.starttls()
           smtp.ehlo()

           smtp.login("noreply.prototypeapp@gmail.com",mailpass)

           subject = "Your vertification code"
           body = seed

           msg = f'Subject: {subject}\n\n{body}'

           smtp.sendmail("noreply.prototypeapp@gmail.com", self.root.get_screen("forgot").ids.mail1.text, msg)
       self.root.current = "forgot2"
           
   def forgot2(self):
       if self.root.get_screen("forgot2").ids.mail1.text == str(seed):
           self.root.current = "forgot3"
       else:
           self.root.get_screen("forgot2").ids.warning_label.text = "Invalid Code"

   def forgot3(self):
       import mysql.connector
       from mysql.connector import Error
       import hashlib as hash

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

dbpass= os.environ.get('dbpass')
mailpass= os.environ.get('mailpass')

   
# Runs the application.
if __name__ == '__main__':
   MainApp().run()

