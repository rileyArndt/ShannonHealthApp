from main import *


        
# Identifies the client's injury
class MyGridLayout(GridLayout):
    # initialize infinite keywords
    def __init__(self, **kwargs):
        #call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        #set comlumns 
        self.cols = 2

        #add widgets
        self.add_widget(Label(text="Injury Type: ", color=(23/255, 135/255, 84/255, 1)))

        # add Input Box
        self.injury = TextInput(multiline=False)
        self.add_widget(self.injury)
        #create a submit button
        self.submit = Button(text="Submit", font_size=32)
        self.submit.background_color=(23/255, 135/255, 84/255, 1)
        #bind the button
        self.submit.bind(on_press=self.press)
        #create button widget
        self.add_widget(self.submit)
        
        self.injury_info = Label()
        self.injury_info.color=(23/255, 135/255, 84/255, 1)
        self.add_widget(self.injury_info)
    
    # Once the client presses the submit button
    # He will see the identification of his injury
    def press(self, instance):
        injury = self.injury.text

        # print(f'Your injury is {injury}')
        self.injury_info.text="Your injury is " + str(injury)
        #clear input boxes
        self.injury.text = ""

# Physical_Screen - Invovles identification of injuries.
class Physical_Screen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
    def on_enter(self, *args):
        self.box = BoxLayout()
        self.box.orientation="vertical"

        self.title_lout = MDFloatLayout()
        self.title_lout.size_hint_y=.11
        self.title_lout.pos_hint={"center_y": .95}
        self.title_lout.md_bg_color=[ 23/255, 135/255, 84/255, 1 ]
    
        # Label for Title Layout
        self.title_label=MDLabel()
        self.title_label.text='Physical Therapy'
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

        self.box.add_widget(self.title_lout)
        self.box.add_widget(MyGridLayout())
        
        self.add_widget(self.box)
        
    def on_leave(self, *args):
        self.clear_widgets()
        
   # Returns to the home page.
    def home_return(self, obj):
        self.manager.current = 'main'
        self.manager.transition.direction = 'right'  