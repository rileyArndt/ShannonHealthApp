from main import *

# The Telemedicine Screen ("TeleScreen")
# provides links when needing quick access
# to telemedicine information.
class TeleScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def on_enter(self):
        # Title Layout that displays the header
        # for the screen.
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
        self.back_btn.bind(on_press=self.go_home)
        self.title_lout.add_widget(self.back_btn)
        
        
        
        self.window = BoxLayout(orientation = 'vertical', padding = 2, spacing = 2)

        self.button = Button(text="Call Provider",
            size_hint=(1,.8),
            background_normal = '',
            font_size = 22,
            background_color = (240/255, 240/255, 240/255, 0.5),
            color = (23/255, 135/255, 84/255, 1)
            )
        self.button.bind(on_press=self.openMC)
        self.window.add_widget(self.button)

        self.button = Button(text="Call Shannon",
            size_hint = (1,.8),
            background_normal = '',
            font_size = 22,
            background_color = (240/255, 240/255, 240/255, 0.5),
            color = (23/255, 135/255, 84/255, 1)
            )
        self.button.bind(on_press=self.openShannon)
        self.window.add_widget(self.button)

        self.button = Button(text="Shannon Telemed",
            size_hint = (1,.8),
            background_normal = '',
            font_size = 22,
            background_color = (240/255, 240/255, 240/255, 0.5),
            color = (23/255, 135/255, 84/255, 1)
            )
        self.button.bind(on_press=self.openShannon)
        self.window.add_widget(self.button)

        self.button=Button(text="Back",
            size_hint=(1,.3),
            background_normal = '',
            font_size = 22,
            background_color = (240/255, 240/255, 240/255, 0.5),
            color = (23/255, 135/255, 84/255, 1)
            
            )
        self.button.bind(on_press=self.go_home)
        self.window.add_widget(self.button)
        
        self.add_widget(self.window)
        self.add_widget(self.title_lout)


        return self.window

    def openMC(self, instance):
        """Takes the client to MyChart"""
        import webbrowser
        webbrowser.open('https://www.mychart.com/')

    def openShannon(self, instance):
        """Takes the client to the Shannon Website"""
        import webbrowser
        webbrowser.open('https://www.shannonhealth.com/')
        
    def go_home(self, obj):
        """Takes the client back to the home screen"""
        self.manager.current = 'main'
        self.manager.transition.direction = 'right'          

