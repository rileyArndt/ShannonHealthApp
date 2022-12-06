# Mitchell Martin
# 10/11/2022


# Adding necessary modules for the kivy
# buildozer to integrate the files.
from Chatbot import chatresponses
from str_builder import *
from main import *
import mods

# The cart displayed on the
# available medications screen
class CartRV(RecycleView):
   def __init__(self, **kwargs):
      super().__init__(**kwargs)

# The database connection to the
# product database.
class RV(RecycleView):
   def __init__(self, **kwargs):
      super().__init__()      # Database Connection
      mydb = mysql.connector.connect(
         host = "shannontestdatabase.cxc8luynmyvm.us-east-1.rds.amazonaws.com",
         user = "admin",
         passwd = dbpass,
         database = "shannon"
      )
      
      c = mydb.cursor()
      
      c.execute("""SELECT * FROM products""")
      records = c.fetchall()     
      content = []
      
      for record in records:
         content.append(record[0] + "        " + record[1] + "        " + record[2] + "        $" + str(record[3]))
      
      i = 0
      for item in content:
         i += 1      
         self.data.append(
         {
            "viewclass": "CustomOneLineIconListItem",
            "icon": "medical-bag",
            "theme_icon_color": 'Custom',
            "icon_color": [23/255, 135/255, 84/255, 1],
            "text": item,
            "index": i
         }
      )   

# The database connection to the
# product database.
# Selects all the products that have been shipped in.
class ReadyRV(RecycleView):
   def __init__(self, **kwargs):
      super().__init__()      # Database Connection
      mydb = mysql.connector.connect(
         host = "shannontestdatabase.cxc8luynmyvm.us-east-1.rds.amazonaws.com",
         user = "admin",
         passwd = dbpass,
         database = "shannon"
      )
      
      c = mydb.cursor()
      
      c.execute("""SELECT id, product_name, branch_name, price, ship_date FROM branch
      INNER JOIN products ON branch.branch_id = products.branch_id
      WHERE shipped = 'Y'
      ORDER BY branch_name""")
      records = c.fetchall()     
      self.content = []
      
      for record in records:
         self.content.append((record[0], record[1], record[2], "$" + str(record[3]), str(record[4])))
      

# The perscription screen's functionality
# is displayed in the str_builder.
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
#          database = "shannon"
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
   
# Shows the most recent products that have been
# shipped in according to the database.
class RecentLayout(MDBoxLayout):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      mydb = mysql.connector.connect(
         host = "shannontestdatabase.cxc8luynmyvm.us-east-1.rds.amazonaws.com",
         user = "admin",
         passwd = dbpass,
         database = "shannon"
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


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
   """Adds selection and focus behavior to our view."""

# Perscriptions Ready Screen:
# Allows the user to see which medications
# have been delivered.
class PersLookScreen(Screen):
   def __init__(self, **kw):
      super().__init__(**kw)
   
   def on_enter(self, *args):
      # Database Connection
      self.mydb = mysql.connector.connect(
         host = "shannontestdatabase.cxc8luynmyvm.us-east-1.rds.amazonaws.com",
         user = "admin",
         passwd = dbpass,
         database = "shannon"
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

      # self.rview = ReadyRV()

      
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
      
      self.checkedbtn=MDRectangleFlatButton()
      self.checkedbtn.text='Mark As Checked Out'
      self.checkedbtn.pos_hint={"center_x": 0.5, "center_y": 0.15}
      self.checkedbtn.size_hint_x=.6
      self.checkedbtn.theme_text_color="Custom"
      self.checkedbtn.line_color=[ 0, 0, 0, 0 ]
      self.checkedbtn.text_color=[ 1, 1, 1, 1 ]
      self.checkedbtn.md_bg_color=[ 23/255, 135/255, 84/255, 1  ]
      self.checkedbtn.bind(on_press=self.remove_rows)

      self.rview = ReadyRV()
      self.table = MDDataTable(
      pos_hint={"center_x": 0.5, "center_y": 0.5},
      background_color_header=[ 23/255, 135/255, 84/255, 1 ],
      background_color_selected_cell=[ 23/255, 135/255, 84/255, .5/1 ],
      check=True,
      padding=dp(15),
      rows_num=15,
      column_data=[
         ("ID", dp(30)),
         ("Name", dp(30)),
         ("Pharmacy", dp(30)),
         ("Price", dp(30)),
         ("Shipped Date", dp(30))
      ],
      row_data=self.rview.content         
      )
            
      
      self.hm = RelativeLayout()
      self.hm.add_widget(self.table)
      self.hm.size_hint_y=.67
      self.hm.pos_hint={"center_x": 0.5, "center_y": 0.5}



      self.inlout.add_widget(self.itxtfield)
      self.txtlout.add_widget(self.inlout)
      self.blout.add_widget(self.txtlout)
      self.add_widget(self.checkedbtn)
      self.blout.add_widget(self.buttons_lout)
      self.add_widget(self.hm)
      self.add_widget(self.blout)
      


      
      return self.blout
   
   def remove_rows(self, obj):
      """Removes the unnecessary rows"""
      rows2remove = self.table.get_row_checks()
      
      for r in rows2remove:
         self.table.remove_row(tuple(r))
   
   def on_leave(self, *args):
      """Clears the widgets"""
      self.clear_widgets()
      
   def get_records(self):
      """Grabs the available records"""
      return self.records
      

   
   def go_back(self, obj):
      """Redirects the the Perscription Control Screen"""
      self.manager.current = 'pscreen'
      self.manager.transition.direction = 'right'
      
   def go_home(self, obj):
      """Takes the client back to the menu."""
      self.manager.current = 'main'
      self.manager.transition.direction = 'right'  
          
   def on_leave(self, *args):
      """Clears the widgets"""
      self.clear_widgets()
      
   def search(self, obj):
      """Filter the medications within the search"""
      self.table.row_data = ()
      for name in self.rview.content:
         if self.itxtfield.text.lower() in name[0].lower() or self.itxtfield.text.lower() in name[1].lower() or self.itxtfield.text.lower() in name[2].lower():
            self.table.row_data.append(name)
            print(name)
            

# The Available Medications Screen:
# Allows the user to order the medications needed.
class AllPersScreen(Screen):
   def __init__(self, **kw):
      super().__init__(**kw)
      
   def on_enter(self, *args):
      # Database Connection
      self.mydb = mysql.connector.connect(
         host = "shannontestdatabase.cxc8luynmyvm.us-east-1.rds.amazonaws.com",
         user = "admin",
         passwd = dbpass,
         database = "shannon"
      )
      
      self.c = self.mydb.cursor()
      
      
      
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
      self.cview = CartRV()
      self.cartlabel=MDLabel()
      self.cartlabel.text='Cart'
      self.cartlabel.color=[ 23/255, 135/255, 84/255, 1 ]
      self.cartlabel.halign="center"
      self.cartlabel.font_style="H4"
      self.cartlabel.font_size="20sp"
      self.cartlabel.pos_hint={"center_x": 0.5, "center_y": 0.7}
      self.cartlabel.size_hint_y=None
      self.cartlabel.height=100
      
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
      
      self.registerbtn=MDRectangleFlatButton()
      self.registerbtn.text='Insert in Cart'
      self.registerbtn.pos_hint={"center_x": 0.5, "center_y": 0.15}
      self.registerbtn.size_hint_x=.6
      self.registerbtn.theme_text_color="Custom"
      self.registerbtn.line_color=[ 0, 0, 0, 0 ]
      self.registerbtn.text_color=[ 1, 1, 1, 1 ]
      self.registerbtn.md_bg_color=[ 23/255, 135/255, 84/255, 1  ]
      self.registerbtn.bind(on_press=self.update_view)
      
      self.submitbtn=MDRectangleFlatButton()
      self.submitbtn.text='Submit'
      self.submitbtn.pos_hint={"center_x": 0.5, "center_y": 0.10}
      self.submitbtn.size_hint_x=.6
      self.submitbtn.theme_text_color="Custom"
      self.submitbtn.line_color=[ 0, 0, 0, 0 ]
      self.submitbtn.text_color=[ 1, 1, 1, 1 ]
      self.submitbtn.md_bg_color=[ 23/255, 135/255, 84/255, 1  ]
      
      self.clearbtn=MDRectangleFlatButton()
      self.clearbtn.text='Clear'
      self.clearbtn.pos_hint={"center_x": 0.5, "center_y": 0.05}
      self.clearbtn.line_color=[ 0, 0, 0, 0 ]
      self.clearbtn.text_color=[ 1, 1, 1, 1 ]
      self.clearbtn.md_bg_color=[ 23/255, 135/255, 84/255, 1  ]
      self.clearbtn.bind(on_press=self.clear)


      self.inlout.add_widget(self.itxtfield)
      self.txtlout.add_widget(self.inlout)
      self.blout.add_widget(self.txtlout)
      self.blout.add_widget(self.rview)
      self.blout.add_widget(self.cartlabel)
      self.blout.add_widget(self.cview)   
      self.add_widget(self.clearbtn)
      self.add_widget(self.submitbtn)
      self.add_widget(self.registerbtn)
      self.blout.add_widget(self.buttons_lout)
      self.add_widget(self.blout)

      return self.blout
   
   def clear(self, obj):
      """Clears the cart."""
      self.cartdb = mysql.connector.connect(
         host = "shannontestdatabase.cxc8luynmyvm.us-east-1.rds.amazonaws.com",
         user = "admin",
         passwd = dbpass,
         database = "shannon"
      )
       
      self.c2 = self.cartdb.cursor()
      query = "DELETE FROM cart WHERE usr_id = '" +  mods.username + "';"
      self.c2.execute(query)
      self.cartdb.commit()
      self.cview.data = []

      
   def update_view(self, obj):
      """Updates the view."""
      connection = mysql.connector.connect(host = "shannontestdatabase.cxc8luynmyvm.us-east-1.rds.amazonaws.com",
      user = "admin",
      passwd =  dbpass)
      self.c2 = connection.cursor()
      self.c2.execute("use shannon;")
      
      self.username = mods.username
      
      f_query = "DELETE FROM cart WHERE product_name IS NULL;"
      self.c2.execute(f_query)
      
      s_query = "SELECT * FROM cart WHERE usr_id = '" + self.username + "';"
      self.c2.execute(s_query)
      self.cview.data = []
      records = self.c2.fetchall()
      for name in records:
         self.cview.data.append(
         {
            "viewclass": "CustomOneLineIconListItem",
            "icon": "medical-bag",
            "text": name[0] + "        " + name[1] + "        " + str(name[2])                
            }
         )
      
   def get_records(self):
      """Returns the available records."""
      return self.cview.data
   
   def on_leave(self, *args):
      """Clears all widgets."""
      self.clear_widgets()
   
   def back(self, obj):
      """Takes the user back to the menu."""
      self.manager.current = 'pscreen'
      self.manager.transition.direction = 'right'
         
   def home(self, obj):
      """Takes the user back to the Menu."""
      self.manager.current = 'main'
      self.manager.transition.direction = 'right'
      
   def search(self, obj):
      """Filters the perscription search."""
      connection = mysql.connector.connect(host = "shannontestdatabase.cxc8luynmyvm.us-east-1.rds.amazonaws.com",
      user = "admin",
      passwd =  dbpass)
      self.c2 = connection.cursor()
      self.c2.execute("use shannon;")
      
      self.rview.data = []
      self.c2.execute("SELECT * FROM products")
      self.records = self.c2.fetchall()
      for name in self.records:
         if self.itxtfield.text.lower() in name[0].lower() or self.itxtfield.text.lower() in name[1].lower() or self.itxtfield.text.lower() in name[2].lower():
            self.rview.data.append(
               {
                  "viewclass": "CustomOneLineIconListItem",
                  "icon": "medical-bag",
                  "text": name[0] + "        " + name[1] + "        " + name[2]                
               }
            )
         
   
      
   def pers_screen(self, obj):
      """Transfers to the perscription screen."""
      self.manager.current = 'pscreen'
      self.manager.transition.direction = 'left'
      
     

     

