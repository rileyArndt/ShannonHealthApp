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

# The MainScreen class's functionality is on kivy. 
#
# Let me know if you
# only want to make a screen using python.
class MainScreen(Screen):
   pass

class NewsList(MDList):
   
   def __init__(self, *args, **kwargs):
      super().__init__(**kwargs)
      items = dataextraction.news_item()
      
      for item in items:
         wig = OneLineIconListItem(text=item)
         imagery = IconLeftWidget(icon='newspaper')
         wig.add_widget(imagery)
         self.add_widget(wig)


class CustomOneLineIconListItem(OneLineIconListItem):
   icon = StringProperty()
   

# Add all your created screens
# to the screen manager.
global sm
sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))

# Builds the application.
class MainApp(MDApp):
   def build(self):
      screen = Builder.load_string(complete_app_builder)
      return screen  
   
# Runs the application.
if __name__ == '__main__':
   MainApp().run()


