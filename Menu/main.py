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
from LoginInfo import *



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
      self.root.current = 'login'
      self.root.direction = 'left'  


MainApp.logger = logger
MainApp.create = create
MainApp.create2 = create2
MainApp.forgot = forgot
MainApp.forgot2 = forgot2
MainApp.forgot3 = forgot3


   
# Runs the application.
if __name__ == '__main__':
   MainApp().run()

