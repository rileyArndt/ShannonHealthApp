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

# Holds the locations of all facilities.
class MapScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # lout is the layout
        self.lout = BoxLayout()
        self.lout.orientation = "vertical"
        # [ 23/255, 135/255, 84/255, 0 ]
        # Title Layout
        self.title_lout = MDFloatLayout()
        self.title_lout.size_hint_y=.11
        self.title_lout.pos_hint={"center_y": .95}
        self.title_lout.md_bg_color=[ 23/255, 135/255, 84/255, 1 ]
    
        # Label for Title Layout
        self.title_label=MDLabel()
        self.title_label.text='Provider Search'
        self.title_label.pos_hint={"center_y": .5}
        self.title_label.halign="center"
        self.title_label.font_size="25sp"
        self.title_label.theme_text_color="Custom"
        self.title_label.text_color=[ 240/255, 240/255, 240/255, 1 ]
        self.title_lout.add_widget(self.title_label)
        
        self.back_btn=MDIconButton()
        self.back_btn.pos_hint={"center_y": .5}
        self.back_btn.icon='keyboard-backspace'
        self.back_btn.halign="left"
        self.back_btn.theme_icon_color="Custom"
        self.back_btn.icon_color=[ 240/255, 240/255, 240/255, 1 ]
        self.back_btn.bind(on_press=self.headback)
        self.title_lout.add_widget(self.back_btn)
        self.lout.add_widget(self.title_lout)

        self.mapview = MapView(zoom = 12, lat = 31.4638, lon = -100.4370)
        self.mapview.double_tap_zoom = True

        # Shannon Medical Center
        self.marker1 = MapMarkerPopup()
        self.marker1.lat = 31.465321
        self.marker1.lon = -100.434753
        # Shannon Medical Center
        self.mapview.add_widget(self.marker1)

        self.medbtn1 = Button()
        self.medbtn1.text = "Shannon Medical Center"
        self.medbtn1.size_hint = [ 2, 0.5 ]

        self.marker1.add_widget(self.medbtn1)
        # Centers map on marker clicked.
        self.marker1.bind(on_press = lambda x: self.mapview.center_on(self.marker1.lat, self.marker1.lon))

        # Shannon Clinic
        self.marker2 = MapMarkerPopup()
        self.marker2.lat = 31.426300
        self.marker2.lon = -100.495770
        # Shannon Clinic
        self.mapview.add_widget(self.marker2)

        self.medbtn2 = Button()
        self.medbtn2.text = "Shannon Clinic"
        self.medbtn2.size_hint = [ 2, 0.5 ]
        self.marker2.add_widget(self.medbtn2)
        # Centers map on marker clicked.
        self.marker2.bind(on_press = lambda x: self.mapview.center_on(self.marker2.lat, self.marker2.lon))

        # Shannon Urgent Care West
        self.marker3 = MapMarkerPopup()
        self.marker3.lat = 31.432950
        self.marker3.lon = -100.500710
        # Urgent Care West
        self.mapview.add_widget(self.marker3)

        self.medbtn3 = Button()
        self.medbtn3.text = "Shannon Urgent Care West"
        self.medbtn3.size_hint = [ 2, 0.5 ]
        self.marker3.add_widget(self.medbtn3)
        # Centers map on marker clicked.
        self.marker3.bind(on_press = lambda x: self.mapview.center_on(self.marker3.lat, self.marker3.lon))

        # Shannon South Hospital
        self.marker4 = MapMarkerPopup()
        self.marker4.lat = 31.418409
        self.marker4.lon = -100.469887
        # South Hospital
        self.mapview.add_widget(self.marker4)

        self.medbtn4 = Button()
        self.medbtn4.text = "Shannon South Hospital"
        self.medbtn4.size_hint = [ 2, 0.5 ]
        self.marker4.add_widget(self.medbtn4)
        # Centers map on marker clicked.
        self.marker4.bind(on_press = lambda x: self.mapview.center_on(self.marker4.lat, self.marker4.lon))

        # Shannon Senior Health Center
        self.marker5 = MapMarkerPopup()
        self.marker5.lat = 31.429410
        self.marker5.lon = -100.478960
        # Senior Health Center
        self.mapview.add_widget(self.marker5)

        self.medbtn5 = Button()
        self.medbtn5.text = "Shannon Senior Health-Center"
        self.medbtn5.size_hint = [ 2, 0.5 ]
        self.marker5.add_widget(self.medbtn5)
        # Centers map on marker clicked.
        self.marker5.bind(on_press = lambda x: self.mapview.center_on(self.marker5.lat, self.marker5.lon))

        # Shannon Clinic South
        self.marker6 = MapMarkerPopup()
        self.marker6.lat = 31.419360
        self.marker6.lon = -100.468500
        # Clinic South
        self.mapview.add_widget(self.marker6)

        self.medbtn6 = Button()
        self.medbtn6.text = "Shannon Clinic South"
        self.medbtn6.size_hint = [ 2, 0.5 ]
        self.marker6.add_widget(self.medbtn6)
        # Centers map on marker clicked.
        self.marker6.bind(on_press = lambda x: self.mapview.center_on(self.marker6.lat, self.marker6.lon))

        # Shannon Clinic South-West
        self.marker7 = MapMarkerPopup()
        self.marker7.lat = 31.436040
        self.marker7.lon = -100.501920
        # Clinic South-West
        self.mapview.add_widget(self.marker7)

        self.medbtn7 = Button()
        self.medbtn7.text = "Shannon Clinic South-West"
        self.medbtn7.size_hint = [ 2, 0.5 ]
        self.marker7.add_widget(self.medbtn7)
        # Centers map on marker clicked.
        self.marker7.bind(on_press = lambda x: self.mapview.center_on(self.marker7.lat, self.marker7.lon))

        # Shannon Clinic
        self.marker8 = MapMarkerPopup()
        self.marker8.lat = 31.463770
        self.marker8.lon = -100.434174
        # Clinic
        self.mapview.add_widget(self.marker8)

        self.medbtn8 = Button()
        self.medbtn8.text = "Shannon Clinic"
        self.medbtn8.size_hint = [ 2, 0.5 ]
        self.marker8.add_widget(self.medbtn8)
        # Centers map on marker clicked.
        self.marker8.bind(on_press = lambda x: self.mapview.center_on(self.marker8.lat, self.marker8.lon))

        # Shannon Urgent Care South
        self.marker9 = MapMarkerPopup()
        self.marker9.lat = 31.420220
        self.marker9.lon = -100.470690
        # Urgent Care South
        self.mapview.add_widget(self.marker9)

        self.medbtn9 = Button()
        self.medbtn9.text = "Shannon Urgent Care South"
        self.medbtn9.size_hint = [ 2, 0.5 ]
        self.marker9.add_widget(self.medbtn9)
        # Centers map on marker clicked.
        self.marker9.bind(on_press = lambda x: self.mapview.center_on(self.marker9.lat, self.marker9.lon))

        # Shannon Health Club
        self.marker10 = MapMarkerPopup()
        self.marker10.lat = 31.420150
        self.marker10.lon = -100.480310
        # Health Club
        self.mapview.add_widget(self.marker10)

        self.medbtn10 = Button()
        self.medbtn10.text = "Shannon Health Club"
        self.medbtn10.size_hint = [ 2, 0.5 ]
        self.marker10.add_widget(self.medbtn10)
        # Centers map on marker clicked.
        self.marker10.bind(on_press = lambda x: self.mapview.center_on(self.marker10.lat, self.marker10.lon))

        # Shannon Clinic Jackson
        self.marker11 = MapMarkerPopup()
        self.marker11.lat = 31.436550
        self.marker11.lon = -100.457060
        # Clinic Jackson
        self.mapview.add_widget(self.marker11)

        self.medbtn11 = Button()
        self.medbtn11.text = "Shannon Clinic Jackson"
        self.medbtn11.size_hint = [ 2, 0.5 ]
        self.marker11.add_widget(self.medbtn11)
        # Centers map on marker clicked.
        self.marker11.bind(on_press = lambda x: self.mapview.center_on(self.marker11.lat, self.marker11.lon))

        # Shannon Business Office
        self.marker12 = MapMarkerPopup()
        self.marker12.lat = 31.468750
        self.marker12.lon = -100.431220
        # Business Office
        self.mapview.add_widget(self.marker12)

        self.medbtn12 = Button()
        self.medbtn12.text = "Shannon Business Office"
        self.medbtn12.size_hint = [ 2, 0.5 ]
        self.marker12.add_widget(self.medbtn12)
        # Centers map on marker clicked.
        self.marker12.bind(on_press = lambda x: self.mapview.center_on(self.marker12.lat, self.marker12.lon))

        self.butnlout = MDFloatLayout()
        self.butnlout.size_hint_y=.13

        self.babtn = MDRectangleFlatButton()
        #self.btn.set_text_color(23/255, 135/255, 84/255, 1)
        self.babtn.text = "More Information on Locations"
        self.babtn.theme_text_color="Custom"
        self.babtn.line_color=[ 0, 0, 0, 0 ]
        self.babtn.text_color=[ 1, 1, 1, 1 ]
        self.babtn.md_bg_color=[ 23/255, 135/255, 84/255, 1 ]
        self.babtn.pos_hint={"center_x": 0.5, "center_y": 0.5}
        self.babtn.bind(on_press = self.openMC)
        self.butnlout.add_widget(self.babtn)

        self.lout.add_widget(self.mapview)
        self.lout.add_widget(self.butnlout)

        self.add_widget(self.lout)

    def openMC(self, instance):
        import webbrowser
        webbrowser.open('https://www.shannonhealth.com/locations.aspx')
        
    def headback(self, instance):
        self.manager.current = 'main'
        self.manager.transition.direction = 'right'  
                  


   
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
# sm.add_widget(MapScreen(name='mapscr'))


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










