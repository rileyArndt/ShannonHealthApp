# Mitchell Martin
# 10/11/2022


# Adding all the modules
from mods import *
from Chatbot import chatresponses as cr
from str_builder import *
from main import *


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
      self.title_lout.md_bg_color=[ 23/255, 135/255, 84/255, 1 ]
   
      # Label for Title Layout
      self.title_label=MDLabel()
      self.title_label.text='Your M.D.'
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
         self.chat_lout.height+=1000   
   
   # Bot's answer
   def bot_answer(self, obj):   
      if len(cr.matchedresponse(self.value)) < 6:
         self.ffsize = .17
         self.halign = "center"
      elif len(cr.matchedresponse(self.value)) < 11:
         self.ffsize = .22
         self.halign = "center"
      elif len(cr.matchedresponse(self.value)) < 16:
         self.ffsize = .24
         self.halign = "center"
      elif len(cr.matchedresponse(self.value)) < 22:
         self.ffsize = .32
         self.halign = "center"
      else:
         self.ffsize = .45
         self.halign = "center"
      self.chat_lout.add_widget(Response(text=cr.matchedresponse(self.value), size_hint_x=self.ffsize, halign=self.halign))
      self.robot_redirect()
   
   def robot_redirect(self):
      # Key : keywords
      try:
         if cr.matchedresponse(self.value) == cr.B_TELEMED:
            webbrowser.open_new_tab('http://www.shannonhealth.com/services/shannon-on-demand-telemedicine/')
         elif cr.matchedresponse(self.value) == cr.B_WEBSITE:
            webbrowser.open_new_tab('https://www.shannonhealth.com/')
         elif cr.matchedresponse(self.value) == cr.B_HOME:
            self.manager.current = 'main'
            self.manager.transition.direction = 'right'
         elif cr.matchedresponse(self.value) == cr.B_MYCHARTLINK:
            webbrowser.open_new_tab('https://www.shannonhealth.com/patients-and-visitors/patient-portal-mychart/')
         elif cr.matchedresponse(self.value) == cr.B_BILL:
            webbrowser.open_new_tab('https://mychart.shannonhealth.org/mychart/Billing/GuestPay/PayasGuest')
         elif cr.matchedresponse(self.value) == cr.B_WEBSITE:
            webbrowser.open_new_tab('https://www.shannonhealth.com/')
         elif cr.matchedresponse(self.value) == cr.B_PHARMACY:
            webbrowser.open_new_tab('https://www.shannonhealth.com/services/pharmacy/')
         elif cr.matchedresponse(self.value) == cr.B_PPAGE:
            self.pers_return()
         elif cr.matchedresponse(self.value) == cr.B_PRICEEST:
            webbrowser.open_new_tab('https://www.shannonhealth.com/patients-and-visitors/pricing-and-estimates/')
         elif cr.matchedresponse(self.value) == cr.B_SLEEP:
            webbrowser.open_new_tab('https://www.shannonhealth.com/services/sleep-center/')
         elif cr.matchedresponse(self.value) == cr.B_CAREER:
            webbrowser.open_new_tab('https://www.shannonhealth.com/employment/?utm_source=loyal&utm_medium=chatbot&utm_campaign=dialog')
         elif cr.matchedresponse(self.value) == cr.B_READY:
            self.ready_return()
         elif cr.matchedresponse(self.value) == cr.B_MR:
            webbrowser.open_new_tab('https://www.shannonhealth.com/patients-and-visitors/request-medical-records/')
      except:
         print("Exception: Not conencted to the internet")
   # Returns to the perscription page.
   def pers_return(self):
      self.manager.current = 'pscreen'
      self.manager.transition.direction = 'left'  
   # Returns to the ready perscription page.
   def ready_return(self):
      self.manager.current = 'allscr'
      self.manager.transition.direction = 'left' 
      
   def on_leave(self, *args):
      self.clear_widgets()



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