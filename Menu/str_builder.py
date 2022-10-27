

complete_app_builder = """
# Add your functional screens here
ScreenManager:
   MainScreen:
   ChatScreen:
   PerscriptionScreen:
   AllPersScreen:
   PersLookScreen:

<CustomOneLineIconListItem>
   IconLeftWidget:
      icon: root.icon
      theme_text_color: "Custom"
      text_color: 23/255, 135/255, 84/255, 1 

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

<ReadyRV>
   name: 'readyrv'
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

<PersLookScreen>
   name: 'perlscr'
   
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
   ScrollView:
      do_scroll_x: False
      do_scroll_y: True
      
      MDBoxLayout:
         orientation: 'vertical' 
         size_hint_y: None
         padding:dp(25)
         height: 1000
         MDBoxLayout:
            size_hint_y:.25
            padding:dp(25)
            MDBoxLayout:
               orientation: "vertical"
               spacing: dp(20)

               MDLabel:
                  text: "Perscription Control"
                  color: 23/255, 135/255, 84/255, 1
                  font_style: "H2"

               MDBoxLayout:
                  adaptive_size: True
                  spacing: dp(10)
                  MDLabel:
                     text: "Home"
                     color: 23/255, 135/255, 84/255, 1
                     text_size:None,None
                     adaptive_width:True
                  MDIconButton:
                     icon:'chevron-down'
                     theme_text_color: "Custom"
                     icon_color: [ 23/255, 135/255, 84/255, 1 ]
                     on_press:
                        root.manager.transition.direction = 'right'
                        root.manager.current = 'main'       


         MDGridLayout:
            size_hint_y:.75
            cols: 2
            padding:dp(15)
            spacing:dp(15)
            ElementCard:
               image: "Icons\cariconhd.png"
               text: "Ready For Pickup"
               on_press:
                  root.manager.transition.direction = 'left'
                  root.manager.current = 'perlscr'
            ElementCard:
               image: "Icons\medicon.png"
               text: "Search for Medications"
               on_press:
                  root.manager.transition.direction = 'left'
                  root.manager.current = 'allscr'

         # MDBoxLayout:
         #    padding:dp(15)

         MDBoxLayout:
            # orientation: 'vertical'

            GraphLayout:
               size_hint_y: None
               # adaptive_size: True
               pos_hint: {"center_x": 0.5, "center_y": 0.70}
               width: 2000
               height: 500
            
               
   MDIconButton:
      text: "Home"
      icon: "home"
      theme_text_color: "Custom"
      icon_color: [ 23/255, 135/255, 84/255, 1 ]
      icon_size: dp(30)
      pos_hint: {"center_x": 0.5, "center_y": 0.1}
      on_press:
         root.manager.transition.direction = 'right'
         root.manager.current = 'main'  


<ElementCard@MDCard>:
   size_hint_y: None
   padding: dp(20)
   radius:dp(25)
   icon:''
   icon_size: dp(30)
   image:''
   text:""
   text_color: 23/255, 135/255, 84/255, 1
   subtext: ''
   items_remaining: ''
   height:dp(175)
   orientation: 'vertical'
   Image:
      source:root.image
      width: 250
      size_hint_y: None
      padding: dp(10)
   MDLabel:
      halign: "center"
      valign: "bottom"
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
         title: "Hello, User"
         halign: "center"
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
                  image: "Icons\phoneicon.png"
                  text: "Telemedicene Visits"
               ElementCard:
                  image: "Icons\perscicon.png"
                  text: "Perscription Availability"
                  on_press:
                     root.manager.transition.direction = 'left'
                     root.manager.current = 'pscreen'    

               ElementCard:
                  image: "Icons\chaticon.png"
                  text: "Search for Providers"
               ElementCard:
                  image: "Icons\laboticon.png"
                  text: "Ask the ChatBot"
                  on_press:
                     root.manager.transition.direction = 'left'
                     root.manager.current = 'chats'  
                     
               MDBoxLayout:
                  size_hint_y: None
                  height: 2000



            
   MDIconButton:
      id : 'chatbot'
      icon: "message-badge"
      theme_icon_color: "Custom"
      icon_color: [ 23/255, 135/255, 84/255, 1 ]
      icon_size: dp(30)
      pos_hint: {"center_x": 0.8, "center_y": 0.1}
      on_press:
         root.manager.transition.direction = 'left'
         root.manager.current = 'chats'

         
   MDIconButton:
      text: "Home"
      icon: "home"
      theme_text_color: "Custom"
      icon_color: [ 23/255, 135/255, 84/255, 1 ]
      icon_size: dp(30)
      pos_hint: {"center_x": 0.5, "center_y": 0.1}
   MDIconButton:
      text: "Perscriptions"
      icon: "medication"
      theme_text_color: "Custom"
      icon_size: dp(30)
      icon_color: [ 23/255, 135/255, 84/255, 1 ]
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
               OneLineIconListItem:
                  text: 'Settings'
                  ImageLeftWidget:
                     icon: 'application-settings'
                  
               OneLineIconListItem:
                  text: 'Logout'
                  ImageLeftWidget:
                     icon: 'logout'
"""


