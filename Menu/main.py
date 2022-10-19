# Mitchell Martin
# 10/11/2022


# Adding all the modules
from turtle import onclick
from mods import *
from chatbot import *


# The MainScreen class's functionality is on kivy. 
#
# Let me know if you
# only want to make a screen using python.
class MainScreen(Screen):
   pass

class PerscriptionScreen(Screen):
   pass

class CustomOneLineIconListItem(OneLineIconListItem):
   icon = StringProperty()

class RV(RecycleView):
   def __init__(self, **kwargs):
      super().__init__()      # Database Connection
      mydb = mysql.connector.connect(
         host = "localhost",
         user = "root",
         passwd = "HeBoreItAll#1",
         database = "perscriptions"
      )
      
      c = mydb.cursor()
      
      c.execute("""SELECT * FROM products""")
      records = c.fetchall()     
      content = []
      
      for record in records:
         content.append(record[0] + "        " + record[1] + "        " + record[2])
      
      for item in content:      
         self.data.append(
         {
            "viewclass": "CustomOneLineIconListItem",
            "icon": "medical-bag",
            "text": item
         }
      )

# The chatbot screen.
class ChatScreen(Screen):
   def __init__(self, **kw):
      super().__init__(**kw)
      
   def on_enter(self, *args):
      # Backdrop Layout
      self.full_lout = MDFloatLayout()
      
      # Title Layout
      self.title_lout = MDFloatLayout()
      self.title_lout.size_hint_y=.11
      self.title_lout.pos_hint={"center_y": .95}
      self.title_lout.md_bg_color=[ 240/255, 240/255, 240/255, 1 ]
   
      # Label for Title Layout
      self.title_label=MDLabel()
      self.title_label.text='Your M.D.'
      self.title_label.pos_hint={"center_y": .5}
      self.title_label.halign="center"
      self.title_label.font_size="25sp"
      self.title_label.theme_text_color="Custom"
      self.title_label.text_color=[ 23/255, 135/255, 84/255, 1 ]
      self.title_lout.add_widget(self.title_label)
      
      self.back_btn=MDIconButton()
      self.back_btn.pos_hint={"center_y": .5}
      self.back_btn.icon='keyboard-backspace'
      self.back_btn.halign="left"
      self.back_btn.theme_icon_color="Custom"
      self.back_btn.icon_color=[ 23/255, 135/255, 84/255, 1 ]
      self.back_btn.bind(on_press=self.home_return)
      self.title_lout.add_widget(self.back_btn)
      
      # Allows the user to scroll down through messages.
      self.view=ScrollView()
      self.view.size_hint_y=.77
      self.view.scroll_y=0
      self.view.pos_hint={"x": 0, "y": .116}
      self.view.do_scroll_x=False
      self.view.do_scroll_y=False
      
      # Layout within "self.view"
      # This layout displays each text.
      self.chat_lout=BoxLayout()
      self.chat_lout.orientation='vertical'
      self.chat_lout.size=(self.full_lout.width, self.full_lout.height)
      self.chat_lout.height=300
      self.chat_lout.width=self.width
      self.chat_lout.adaptive_size=True
      self.chat_lout.size_hint=[ None, None ]
      self.chat_lout.pos_hint={'top': 10}
      self.chat_lout.cols=1
      self.chat_lout.spacing=3
   
      
      # Tool Layout
      self.toolbar=MDFloatLayout()
      self.toolbar.md_bg_color=[ 240/255, 240/255, 240/255, 1 ]
      self.toolbar.size_hint_y=.11
      
      self.txt_lout=MDFloatLayout()
      self.txt_lout.size_hint=[ .01, .01 ] #
      self.txt_lout.pos_hint={"center_x": .43, "center_y": .1} #
      with self.txt_lout.canvas:
         clr=Color()
         clr.rgb=[ 240/255, 240/255, 240/255, 1 ]
         rct=RoundedRectangle()
         rct.size=self.pos #
         rct.pos=self.pos
         rct.radius=[ 24, 24, 24, 24 ]
      
      # Message Bar
      self.txtinpt=TextInput()
      self.txtinpt.hint_text="Type a message"
      self.txtinpt.pos_hint={"center_x":.5, "center_y":.5} #
      self.txtinpt.font_size="18sp"
      self.txtinpt.height=self.txtinpt.minimum_height
      self.txtinpt.multiline=False
      self.txtinpt.cursor_color=[ 12/255, 110/255, 90/255, 1 ]
      self.txtinpt.cursor_width="2sp"
      self.txtinpt.foreground_color=[ 23/255, 135/255, 84/255, 1 ]
      self.txtinpt.background_color=[ 0, 0, 0, 0 ]
      self.txtinpt.padding=15
      
      # Button
      self.cbtn=MDIconButton()
      self.cbtn.icon="send"
      self.cbtn.pos_hint={"center_x": .9, "center_y": .055}
      self.cbtn.user_font_size="18sp"
      self.cbtn.theme_text_color="Custom"
      self.cbtn.text_color=[ 1, 1, 1, 1 ]
      self.cbtn.md_bg_color=[ 0, 178/255, 124/255, 1 ]  
      
      self.cbtn.bind(on_press=self.send)  
      
      self.toolbar.add_widget(self.txtinpt)
      self.toolbar.add_widget(self.txt_lout)
      
      self.full_lout.add_widget(self.title_lout)
      self.view.add_widget(self.chat_lout)
      self.full_lout.add_widget(self.view)
      self.full_lout.add_widget(self.toolbar)
      self.full_lout.add_widget(self.cbtn)
      self.add_widget(self.full_lout)
   
      # Bot Greeting
      val = "Hi there! Welcome to Shannon. Can I help answer something for you?"
      self.chat_lout.add_widget(Response(text=val, size_hint_x=.34, halign="center"))    
      
      return self.full_lout
   
   # Returns to the home page.
   def home_return(self, obj):
      self.manager.current = 'main'
      self.manager.transition.direction = 'right'      
   
   # User's command
   def send(self, obj):
      if self.txtinpt.text != "":
         self.value = self.txtinpt.text
         if len(self.value) < 6:
            self.fsize = .17
            self.halign = "center"
         elif len(self.value) < 11:
            self.fsize = .22
            self.halign = "center"
         elif len(self.value) < 16:
            self.fsize = .24
            self.halign = "center"
         elif len(self.value) < 22:
            self.fsize = .28
            self.halign = "center"
         else:
            self.fsize = .30
            self.halign = "center"
         self.chat_lout.add_widget(Command(text=self.value, size_hint_x=self.fsize, halign=self.halign))
         Clock.schedule_once(self.bot_answer, 0.1)
         self.txtinpt.text = ""  
         self.view.do_scroll_y=True
         self.chat_lout.height+=100   
   
   # Bot's answer
   def bot_answer(self, obj):   
      if len(matchedresponse(self.value)) < 6:
         self.ffsize = .17
         self.halign = "center"
      elif len(matchedresponse(self.value)) < 11:
         self.ffsize = .22
         self.halign = "center"
      elif len(matchedresponse(self.value)) < 16:
         self.ffsize = .24
         self.halign = "center"
      elif len(matchedresponse(self.value)) < 22:
         self.ffsize = .32
         self.halign = "center"
      else:
         self.ffsize = .45
         self.halign = "center"
      self.chat_lout.add_widget(Response(text=matchedresponse(self.value), size_hint_x=self.ffsize, halign=self.halign))
      
      # Key : keywords
      if matchedresponse(self.value) == B_TELEMED:
         webbrowser.open_new_tab('http://www.shannonhealth.com/services/shannon-on-demand-telemedicine/')
      elif matchedresponse(self.value) == B_WEBSITE:
         webbrowser.open_new_tab('https://www.shannonhealth.com/')
      elif matchedresponse(self.value) == B_HOME:
         self.manager.current = 'main'
         self.manager.transition.direction = 'right'
      elif matchedresponse(self.value) == B_MYCHARTLINK:
         webbrowser.open_new_tab('https://www.shannonhealth.com/patients-and-visitors/patient-portal-mychart/')
      elif matchedresponse(self.value) == B_BILL:
         webbrowser.open_new_tab('https://mychart.shannonhealth.org/mychart/Billing/GuestPay/PayasGuest')
      elif matchedresponse(self.value) == B_WEBSITE:
         webbrowser.open_new_tab('https://www.shannonhealth.com/')
         

   def on_leave(self, *args):
      self.clear_widgets()

# THe perscription screen
class AllPersScreen(Screen):
   def __init__(self, **kw):
      super().__init__(**kw)
      
   def on_enter(self, *args):
      # Database Connection
      self.mydb = mysql.connector.connect(
         host = "localhost",
         user = "root",
         passwd = "HeBoreItAll#1",
         database = "perscriptions"
      )
      
      self.c = self.mydb.cursor()
      
      self.c.execute("""SELECT * FROM products""")
      self.records = self.c.fetchall()     
      
      
      self.blout = MDBoxLayout()
      self.blout.orientation='vertical'
      self.blout.spacing=dp(10)
      self.blout.padding=dp(20)
      
      self.txtlout=MDBoxLayout()
      self.txtlout.adaptive_height=True
      self.txtlout.orientation='vertical'
      
      
      self.inlout=MDBoxLayout()
      
      self.ibtn=MDIconButton()
      self.ibtn.icon='magnify'
      self.inlout.add_widget(self.ibtn)

      
      self.rview = RV()

      
      self.itxtfield=MDTextField()
      self.itxtfield.hint_text='Search Item'      
      self.nlabel=MDLabel()
      self.nlabel.text='Available Medications'
      self.nlabel.font_style="H4"
      self.nlabel.pos_hint={"center_x": 0.53, "center_y": 0.5}
      self.ibtn.bind(on_press=self.search)
      self.txtlout.add_widget(self.nlabel)
      
      
      self.buttons_lout=RelativeLayout()
      self.buttons_lout.orientation='horizontal'
      self.buttons_lout.height=100
      
      self.backbtn=MDIconButton()
      self.backbtn.icon='backspace'
      self.backbtn.theme_text_color="Custom"
      self.backbtn.icon_color=[ 0, .8, .4, 1  ]
      self.backbtn.pos_hint={"center_x": 0.3, "center_y": 0.1}
      self.backbtn.bind(on_press=self.back)
      self.backbtn.icon_size=dp(30)
      self.buttons_lout.add_widget(self.backbtn)
      
      self.homebtn=MDIconButton()
      self.homebtn.icon='home'
      self.homebtn.theme_text_color="Custom"
      self.homebtn.icon_color=[ 0, .8, .4, 1  ]
      self.homebtn.pos_hint={"center_x": 0.7, "center_y": 0.1}
      self.homebtn.icon_size=dp(30)
      self.homebtn.bind(on_press=self.home)
      self.buttons_lout.add_widget(self.homebtn)


      self.inlout.add_widget(self.itxtfield)
      self.txtlout.add_widget(self.inlout)
      self.blout.add_widget(self.txtlout)
      self.blout.add_widget(self.rview)   
      self.blout.add_widget(self.buttons_lout)
      self.add_widget(self.blout)
      


      
      return self.blout
   
   def on_leave(self, *args):
      self.clear_widgets()
   
   def back(self, obj):
      self.manager.current = 'pscreen'
      self.manager.transition.direction = 'right'
         
   def home(self, obj):
      self.manager.current = 'main'
      self.manager.transition.direction = 'right'
      
   def search(self, obj):
      self.rview.data = []
      for name in self.records:
         if self.itxtfield.text.lower() in name[0].lower() or self.itxtfield.text.lower() in name[1].lower() or self.itxtfield.text.lower() in name[2].lower():
            self.rview.data.append(
               {
                  "viewclass": "CustomOneLineIconListItem",
                  "icon": "medical-bag",
                  "text": name[0] + "        " + name[1] + "        " + name[2]                
               }
            )
            print(name)
         
   
      
   def pers_screen(self, obj):
      self.manager.current = 'pscreen'
      self.manager.transition.direction = 'right'
      
      

# User's command
class Command(MDLabel):
   text = StringProperty()
   size_hint_x = NumericProperty()
   halign = StringProperty()
   font_size = 17

# Chatbot Response
class Response(MDLabel):
   text = StringProperty()
   size_hint_x = NumericProperty()
   halign = StringProperty()
   font_size = 17      



str = """
# Add your functional screens here
ScreenManager:
   MainScreen:
   ChatScreen:
   PerscriptionScreen:
   AllPersScreen:

<CustomOneLineIconListItem>
   IconLeftWidget:
      icon: root.icon
      theme_text_color: "Custom"
      text_color: 0, .8, .4, 1 

<RV>
   name: 'rv'
   key_viewclass: 'viewclass'
   key_size: 'height' 
   
   RecycleBoxLayout:
      default_size: None, dp(48)
      default_size_hint: 1, None
      padding: dp(10)
      size_hint_y: None
      height: self.minimum_height
      orientation: 'vertical'
   

<AllPersScreen>
   name: 'allscr'



<Command>
   size_hint_y: None   
   pos_hint: {"x": .68}
   height: self.texture_size[1]
   padding: 12, 10
   theme_text_color: "Custom"
   text_color: 0, 0, 0, 1
   canvas.before:
      Color:
         rgb: (240/255, 240/255, 240/255, 1)
      RoundedRectangle:
         size: self.size
         pos: self.pos
         radius: [23, 23, 23, 0]
<Response>
   size_hint_y: None
   pos_hint: {"x": .02}
   height: self.texture_size[1]
   padding: 12, 10
   theme_text_color: "Custom"
   text_color: 1, 1, 1, 1
   canvas.before:
      Color:
         rgb: (23/255, 135/255, 84/255, 1)
      RoundedRectangle:
         size: self.size
         pos: self.pos
         radius: [23, 23, 23, 0]

<PerscriptionScreen>:
   name: 'pscreen'
   MDBoxLayout:
      orientation: 'vertical' 
      MDBoxLayout:
         size_hint_y:.25
         padding:dp(25)
         MDBoxLayout:
            orientation: "vertical"
            MDLabel:
               text: "Perscription Control"
               font_style: "H4"
            MDBoxLayout:
               adaptive_size: True
               spacing: dp(10)
               MDLabel:
                  text: "Home"
                  text_size:None,None
                  adaptive_width:True
               MDIconButton:
                  icon:'chevron-down'
                  on_press:
                     root.manager.transition.direction = 'right'
                     root.manager.current = 'main'    
      MDGridLayout:
         size_hint_y:.75
         cols: 2
         padding:dp(15)
         spacing:dp(15)
         ElementCard:
            image: "image.png"
            text: "Perscription Lookup"
         ElementCard:
            image: "image.png"
            text: "Medication List"
            on_press:
               root.manager.transition.direction = 'left'
               root.manager.current = 'allscr'                
         ElementCard:
            image: "image.png"
            text: "Perscription Lookup"
            subtext: "10/15/2022"
         ElementCard:
            image: "image.png"
            text: "Perscription Availability"
            subtext: "10/15/2022"
            items_remaining: '1 Remaining'
   MDIconButton:
      text: "Home"
      icon: "home"
      theme_text_color: "Custom"
      icon_color: [ 0, .8, .4, 1 ]
      icon_size: dp(30)
      pos_hint: {"center_x": 0.5, "center_y": 0.1}
      on_press:
         root.manager.transition.direction = 'right'
         root.manager.current = 'main'  


<ElementCard@MDCard>:
   size_hint_y: None
   padding: dp(20)
   radius:dp(25)
   image:''
   text:""
   text_color: 23/255, 135/255, 84/255, 1
   subtext: ''
   items_remaining: ''
   height:dp(175)
   orientation: 'vertical'
   Image:
      source:root.image
   MDLabel:
      halign: "center"
      text: root.text
   MDLabel:
      halign: "center"
      text: root.subtext
      font_style:"H6"
   MDLabel:
      halign: "center"
      text: root.items_remaining


<ChatScreen>:
   name: 'chats'
   
<MainScreen>:
   name: 'main'
   FloatLayout:
      MDTopAppBar:
         id: 'topbar'
         pos_hint: {"top": 1}
         title: "Test"
         specific_text_color: [ 23/255, 135/255, 84/255, 1 ]
         font_style: "H4"
         md_bg_color: [ 240/255, 240/255, 240/255, 1 ]
         elevation: 8
         left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

   MDBoxLayout:
      pos_hint_y: {"top": 0.23}
      size_hint: [ 1.0, 0.9 ]
      ScrollView:
         do_scroll_y: True
         do_scroll_x: False  
         MDBoxLayout:
            size_hint_y: None
            height: 2000            # can increase if necessary

            MDBoxLayout:
               adaptive_size: True
               spacing: dp(10)
            MDGridLayout:
               size_hint_y:0.99
               cols: 2
               padding:dp(15)
               spacing:dp(15)
               ElementCard:
                  image: "image.png"
                  text: "Telemedicene Visits"
               ElementCard:
                  image: "image.png"
                  text: "Perscription Availability"
                  on_press:
                     root.manager.transition.direction = 'left'
                     root.manager.current = 'pscreen'    

               ElementCard:
                  image: "image.png"
                  text: "Perscription Lookup"
               ElementCard:
                  image: "image.png"
                  text: "Ask the ChatBot"
                  on_press:
                     root.manager.transition.direction = 'left'
                     root.manager.current = 'chats'  



            
   MDIconButton:
      id : 'chatbot'
      icon: "message-badge"
      theme_icon_color: "Custom"
      icon_color: [ 0, .8, .4, 1 ]
      icon_size: dp(30)
      pos_hint: {"center_x": 0.8, "center_y": 0.1}
      on_press:
         root.manager.transition.direction = 'left'
         root.manager.current = 'chats'

         
   MDIconButton:
      text: "Home"
      icon: "home"
      theme_text_color: "Custom"
      icon_color: [ 0, .8, .4, 1 ]
      icon_size: dp(30)
      pos_hint: {"center_x": 0.5, "center_y": 0.1}
   MDIconButton:
      text: "Perscriptions"
      icon: "medication"
      theme_text_color: "Custom"
      icon_size: dp(30)
      icon_color: [ 0, .8, .4, 1 ]
      pos_hint: {"center_x": 0.2, "center_y": 0.1}
      on_press:
         root.manager.transition.direction = 'left'
         root.manager.current = 'pscreen'         

   MDNavigationDrawer:
      id: nav_drawer
      
      BoxLayout:
         orientation: 'vertical'
         spacing: '8dp'
         padding: '8dp'
         
         
         MDLabel:
            text: 'This is a test'
            font_style: 'Subtitle1'
            size_hint_y: None
            height: self.texture_size[1]
            
         MDLabel:
            text: '  justatest@angelo.edu'
            font_style: 'Caption'
            size_hint_y: None
            height: self.texture_size[1]
        
         ScrollView:
            MDList:
               OneLineListItem:
                  text: 'Profile'
               OneLineListItem:
                  text: 'Settings'
               OneLineListItem:
                  text: 'Logout'
"""

# Add all your created screens
# to the screen manager.
global sm
sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))

# Builds the application.
class MainApp(MDApp):
   def build(self):
      screen = Builder.load_string(str)
      return screen  
   
# Runs the application.
if __name__ == '__main__':
   MainApp().run()
