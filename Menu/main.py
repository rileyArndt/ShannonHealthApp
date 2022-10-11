# Mitchell Martin
# 10/11/2022


# Adding all the modules
from mods import *


# The MainScreen class's functionality is on kivy. 
#
# Let me know if you
# only want to make a screen using python.
class MainScreen(Screen):
   pass

  
  
str = """
# Add your functional screens here
ScreenManager:
   MainScreen:



<MainScreen>:
   name: 'main'
   FloatLayout:
      MDTopAppBar:
         pos_hint: {"top": 1}
         title: "Test"
         md_bg_color: [ 0, .8, .4, 1 ]
         elevation: 8
         left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
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

   MDBoxLayout:
      pos_hint_y: {"top": 0.23}
      size_hint: [ 1.0, 0.9 ]
      ScrollView:
         # do_scroll_y: True
         # do_scroll_x: False  
         MDBoxLayout:
            size_hint_y: None
            height: 2000
"""

# Add all your created screens
# to the screen manager.
global sm
sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))

class MainApp(MDApp):
   def build(self):
      screen = Builder.load_string(str)
      return screen  
   
if __name__ == '__main__':
   MainApp().run()
