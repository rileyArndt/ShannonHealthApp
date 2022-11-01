# Mitchell Martin
# 10/11/2022


# Adding all the modules
from matplotlib.patches import Rectangle
from matplotlib.pyplot import bar
from matplotlib.ticker import MaxNLocator
from Chatbot import chatresponses
from str_builder import *
from main import *

class RV(RecycleView):
   def __init__(self, **kwargs):
      super().__init__()      # Database Connection
      mydb = mysql.connector.connect(
         host = "localhost",
         user = "test_user",
         passwd = "pass",
         database = "testing_features"
      )
      
      c = mydb.cursor()
      
      c.execute("""SELECT * FROM products""")
      records = c.fetchall()     
      content = []
      
      for record in records:
         content.append(record[0] + "        " + record[1] + "        " + record[2] + "        $" + str(record[3]))
      
      for item in content:      
         self.data.append(
         {
            "viewclass": "CustomOneLineIconListItem",
            "icon": "medical-bag",
            "theme_icon_color": 'Custom',
            "icon_color": [23/255, 135/255, 84/255, 1],
            "text": item
         }
      )   


class ReadyRV(RecycleView):
   def __init__(self, **kwargs):
      super().__init__()      # Database Connection
      mydb = mysql.connector.connect(
         host = "localhost",
         user = "test_user",
         passwd = "pass",
         database = "testing_features"
      )
      
      c = mydb.cursor()
      
      c.execute("""SELECT * FROM products""")
      records = c.fetchall()     
      content = []
      
      for record in records:
         content.append(record[0] + "        " + record[1] + "        " + record[2] + "        $" + str(record[3]))
      
      for item in content:      
         self.data.append(
         {
            "viewclass": "CustomOneLineIconListItem",
            "icon": "medical-bag",
            "theme_icon_color": 'Custom',
            "icon_color": [23/255, 135/255, 84/255, 1],
            "text": item
         }
      )   


class PerscriptionScreen(Screen):
   pass

# class GraphLayout(MDBoxLayout):
#    def __init__(self, *args, **kwargs):
#       super().__init__(*args, **kwargs)
#       # Database Connection
#       mydb = mysql.connector.connect(
#          host = "localhost",
#          user = "test_user",
#          passwd = "pass",
#          database = "testing_features"
#       )
      
#       c = mydb.cursor()

#       c.execute("SELECT branch_name, COUNT(*) FROM products INNER JOIN branch ON branch.branch_id = products.branch_id GROUP BY branch_name")
#       records = c.fetchall()     
      
#       values = {}
#       for record in records:
#          values[record[0]] = record[1]
         
#       pharmacy = list(values.keys())
#       quantity = list(values.values())
#       plt.style.use('ggplot')
#       plt.bar(pharmacy, quantity, color='green', width=0.5, )
#       print(values)
      
#       bar_title = MDLabel()
#       bar_title.text = 'Pharmacy Distribution'
#       bar_title.font_style='H5'
#       bar_title.pos_hint = {'center_x': 0.6, 'center_y': 0.47}
#       bar_title.color=[ 23/255, 135/255, 84/255, 1 ]
      
#       self.n_lout = MDFloatLayout()
#       self.n_lout.orientation='vertical'
#       self.n_lout.padding='5px'
#       self.n_lout.pos_hint={"center_x": 0.8, "center_y": 0.9}
#       self.n_lout.add_widget(bar_title)
#       self.n_lout.add_widget(FigureCanvasKivyAgg(plt.gcf()))
#       self.add_widget(self.n_lout)      
   
class RecentLayout(MDBoxLayout):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      mydb = mysql.connector.connect(
         host = "localhost",
         user = "test_user",
         passwd = "pass",
         database = "testing_features"
      )
      
      c = mydb.cursor()

      c.execute("""SELECT product_name, branch_name, ship_date FROM products INNER JOIN
      branch ON branch.branch_id = products.branch_id
      WHERE shipped = 'Y' AND ship_date >= NOW()-INTERVAL 3 MONTH
      ORDER BY ship_date DESC""")
      records = c.fetchall()     
      
      
      self.r_list = MDList() 
      # self.r_list.pos_hint={"center_x": 0.5, "center_y": 0.99}
      
      for record in records:
         self.r_list.add_widget(ThreeLineIconListItem(
            IconLeftWidget(
               icon="medication",
               theme_icon_color="Custom",
               icon_color=[23/255, 135/255, 84/255, 1]
            ),
            text=record[0],
            secondary_text=record[1],
            tertiary_text=str(record[2]),
         ))
      self.add_widget(self.r_list)


class PersLookScreen(Screen):
   def __init__(self, **kw):
      super().__init__(**kw)
   
   def on_enter(self, *args):
      # Database Connection
      self.mydb = mysql.connector.connect(
         host = "localhost",
         user = "test_user",
         passwd = "pass",
         database = "testing_features"
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
      # self.txtlout.md_bg_color=[ 23/255, 135/255, 84/255, 1  ]

      
      self.inlout=MDBoxLayout()
      
      self.ibtn=MDIconButton()
      self.ibtn.icon='magnify'
      self.inlout.add_widget(self.ibtn)

      
      self.rview = ReadyRV()

      
      self.itxtfield=MDTextField()
      self.itxtfield.hint_text='Search Item'      
      self.nlabel=MDLabel()
      self.nlabel.text='Perscriptions Ready'
      self.nlabel.color=[ 23/255, 135/255, 84/255, 1 ]
      self.nlabel.font_style="H4"
      self.nlabel.font_size="25sp"
      self.nlabel.halign="center"
      self.nlabel.pos_hint={"center_x": 0.5, "center_y": 0.5}
      self.ibtn.bind(on_press=self.search)
      self.txtlout.add_widget(self.nlabel)
      
      
      self.buttons_lout=RelativeLayout()
      self.buttons_lout.orientation='horizontal'
      self.buttons_lout.height=100
      
      self.backbtn=MDIconButton()
      self.backbtn.icon='backspace'
      self.backbtn.theme_text_color="Custom"
      self.backbtn.icon_color=[ 23/255, 135/255, 84/255, 1  ]
      self.backbtn.pos_hint={"center_x": 0.3, "center_y": 0.1}
      self.backbtn.bind(on_press=self.go_back)
      self.backbtn.icon_size=dp(30)
      self.buttons_lout.add_widget(self.backbtn)
      
      self.homebtn=MDIconButton()
      self.homebtn.icon='home'
      self.homebtn.theme_text_color="Custom"
      self.homebtn.icon_color=[ 23/255, 135/255, 84/255, 1  ]
      self.homebtn.pos_hint={"center_x": 0.7, "center_y": 0.1}
      self.homebtn.icon_size=dp(30)
      self.homebtn.bind(on_press=self.go_home)
      self.buttons_lout.add_widget(self.homebtn)


      self.inlout.add_widget(self.itxtfield)
      self.txtlout.add_widget(self.inlout)
      self.blout.add_widget(self.txtlout)
      self.blout.add_widget(self.rview)   
      self.blout.add_widget(self.buttons_lout)
      self.add_widget(self.blout)
      


      
      return self.blout
   
   def go_back(self, obj):
      self.manager.current = 'pscreen'
      self.manager.transition.direction = 'right'
      
   def go_home(self, obj):
      self.manager.current = 'main'
      self.manager.transition.direction = 'right'  
          
   def on_leave(self, *args):
      self.clear_widgets()
      
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
            

# THe perscription screen
class AllPersScreen(Screen):
   def __init__(self, **kw):
      super().__init__(**kw)
      
   def on_enter(self, *args):
      # Database Connection
      self.mydb = mysql.connector.connect(
         host = "localhost",
         user = "test_user",
         passwd = "pass",
         database = "testing_features"
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
      # self.txtlout.md_bg_color=[ 23/255, 135/255, 84/255, 1  ]

      
      self.inlout=MDBoxLayout()
      
      self.ibtn=MDIconButton()
      self.ibtn.icon='magnify'
      self.inlout.add_widget(self.ibtn)

      
      self.rview = RV()

      
      self.itxtfield=MDTextField()
      self.itxtfield.hint_text='Search Item'      
      self.nlabel=MDLabel()
      self.nlabel.text='Available Medications'
      self.nlabel.color=[ 23/255, 135/255, 84/255, 1 ]
      self.nlabel.font_style="H4"
      self.nlabel.font_size="25sp"
      self.nlabel.halign="center"
      self.nlabel.pos_hint={"center_x": 0.5, "center_y": 0.5}
      self.ibtn.bind(on_press=self.search)
      self.txtlout.add_widget(self.nlabel)
      
      
      self.buttons_lout=RelativeLayout()
      self.buttons_lout.orientation='horizontal'
      self.buttons_lout.height=100
      
      self.backbtn=MDIconButton()
      self.backbtn.icon='backspace'
      self.backbtn.theme_text_color="Custom"
      self.backbtn.icon_color=[ 23/255, 135/255, 84/255, 1  ]
      self.backbtn.pos_hint={"center_x": 0.3, "center_y": 0.1}
      self.backbtn.bind(on_press=self.back)
      self.backbtn.icon_size=dp(30)
      self.buttons_lout.add_widget(self.backbtn)
      
      self.homebtn=MDIconButton()
      self.homebtn.icon='home'
      self.homebtn.theme_text_color="Custom"
      self.homebtn.icon_color=[ 23/255, 135/255, 84/255, 1  ]
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
      self.manager.transition.direction = 'left'
      
     
