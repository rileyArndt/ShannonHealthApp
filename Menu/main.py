# Mitchell Martin
# 10/11/2022

# Adding all the modules
from mods import *
from str_builder import *
from Perscription import perscreen
from Chatbot import chatresponses, chatai, dataextraction
from LoginInfo import *

from kivymd.icon_definitions import md_icons
from kivymd import icon_definitions
import kivymd.uix.navigationdrawer
from mysql.connector.locales.eng import client_error
import mysql
import kivymd.uix.datatables
import kivymd.uix.dropdownitem
from mysql.connector import Error
import geocoder
import socket
import datetime
import hashlib as hash
import mods



dbpass= os.environ.get('dbpass')
mailpass= os.environ.get('mailpass')

# The Login class's functionality is on kivy. 
class Login (Screen):
    pass

# The MainScreen class's functionality is on kivy. 
class MainScreen(Screen):
   pass

# The Create, Create2, Forgot, Forgot2 class's functionality is on kivy. 
# Create, Create2 - Creates an account for a user.
# Forgot, Forgot2, Forgot3 - Helps the user find their lost account. 
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

class Physical_Screen(Screen):
   pass

   
mods.username = 'default'

# The user logs in to the application
# by using the "logger" function.
def logger(self):
   
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

   mods.username = str(self.root.get_screen("login").ids.user.text)
   
   while '@' not in mods.username or '.' not in mods.username:
       self.root.get_screen("login").ids.warning_label.text = "please enter a valid email"
       return
   secret = str(self.root.get_screen("login").ids.password.text)
   sal = grabQuery(""" 
   select sal from auth 
   where email = '""" + mods.username +"';")
   if len(sal) > 0:
       sal = sal[0][0]
       secret = hash.md5((sal + secret).encode())   #placeholder
       secret = secret.hexdigest()
       if secret == grabQuery("select phash from auth where email='" + mods.username + "';")[0][0]: 
           city = geocoder.ip("me").city
           realip = socket.gethostbyname(socket.gethostname())
           time = str(datetime.datetime.now())[:-7]
           insertQuery("update auth set location = '" + city + "', ip = '" + realip+"', logintime = '" + time + "' where email = '"+ mods.username+ "';")
           insertQuery("insert into cart(usr_id) values ('" + mods.username + "');")
           self.root.current = 'main'
           print(mods.username)
           return 
       else:
           self.root.get_screen("login").ids.warning_label.text = "Could not authenticate user, please re-enter your credentials."
           return 
   else:
       self.root.get_screen("login").ids.warning_label.text = "Could not authenticate user, please re-enter your credentials."
       return 


   

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
      self.root.current = 'login'
      self.root.direction = 'left'  
    
# Contains the Login Functionality
# of the LoginInfo .py file.
MainApp.logger = logger
MainApp.create = create
MainApp.create2 = create2
MainApp.forgot = forgot
MainApp.forgot2 = forgot2
MainApp.forgot3 = forgot3


# Returns the username.
def user_name():
  return sm.get_screen("login").ids.user.text

# Connection to the user's product cart.
# Holds all the products a customer
# wants to buy.
class CustomOneLineIconListItem(OneLineIconListItem):
   icon = StringProperty()
   

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      
   def print_item(self, instance):
      self.cartdb = mysql.connector.connect(
         host = "shannontestdatabase.cxc8luynmyvm.us-east-1.rds.amazonaws.com",
         user = "admin",
         passwd = dbpass,
         database = "shannon"
      )
      
      self.c2 = self.cartdb.cursor()
      query = "INSERT INTO cart SELECT id, product_name, price, '" + mods.username + "' FROM products WHERE id = '" + instance.text[:6] + "'"
      print(query)
      self.c2.execute(query)
      self.cartdb.commit()


    

# Runs the application.
if __name__ == '__main__':
   MainApp().run()










