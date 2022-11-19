import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # initialize infinite keywords
    def __init__(self, **kwargs):
        #call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        #set comlumns 
        self.cols = 2

        #add widgets
        self.add_widget(Label(text="Injury Type: ", color=[.5, .5, .5, 1]))
        # add Input Box
        self.injury = TextInput(multiline=False)
        self.add_widget(self.injury)
        #create a submit button
        self.submit = Button(text="Submit", font_size=32)
        #bind the button
        self.submit.bind(on_press=self.press)
        #create button widget
        self.add_widget(self.submit)
    def press(self, instance):
        injury = self.injury.text

        # print(f'Your injury is {injury}')
        self.add_widget(Label(text=f'Your injury is {injury}', color=[.5, .5, .5, 1]))
        #clear input boxes
        self.injury.text = ""