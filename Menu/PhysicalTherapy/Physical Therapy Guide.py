import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyGridLayout(GridLayout):
    # initialize infinite keywords
    def __init__(self, **kwargs):
        #call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        
        #set comlumns 
        self.cols = 1

        #create injured input layout
        self.injured_area = GridLayout()
        self.injured_area.cols = 1
        #main exercise widget
        self.exercises = GridLayout()
        self.exercises.cols = 1
        #exercise widgets
        #leg
        self.leg_exercises = GridLayout()
        self.leg_exercises.cols = 2
        self.leg_exercises.add_widget(Label(text = "Arm Exercise 1", font_size =32))
        self.leg_exercises.add_widget(Label(text = "Arm Exercise 2", font_size =32))
        self.leg_exercises.add_widget(Label(text = "Arm Exercise 3", font_size =32))
        self.leg_exercises.add_widget(Label(text = "Arm Exercise 4", font_size =32))
        self.leg_exercises.add_widget(Label(text = "Arm Exercise 5", font_size =32))
        
        #arm
        self.arm_exercises = GridLayout()
        self.arm_exercises.cols = 2
        self.arm_exercises.add_widget(Label(text = "Arm Exercise 1", font_size =32))
        self.arm_exercises.add_widget(Label(text = "Arm Exercise 2", font_size =32))
        self.arm_exercises.add_widget(Label(text = "Arm Exercise 3", font_size =32))
        self.arm_exercises.add_widget(Label(text = "Arm Exercise 4", font_size =32))
        self.arm_exercises.add_widget(Label(text = "Arm Exercise 5", font_size =32))
        
        #shoulder
        self.shoulder_exercises = GridLayout()
        self.shoulder_exercises.cols = 2
        self.shoulder_exercises.add_widget(Label(text = "Shoulder Exercise 1", font_size =32))
        self.shoulder_exercises.add_widget(Label(text = "Shoulder Exercise 2", font_size =32))
        self.shoulder_exercises.add_widget(Label(text = "Shoulder Exercise 3", font_size =32))
        self.shoulder_exercises.add_widget(Label(text = "Shoulder Exercise 4", font_size =32))
        self.shoulder_exercises.add_widget(Label(text = "Shoulder Exercise 5", font_size =32))
        #invalid input
        self.invalid_injury = GridLayout()
        self.invalid_injury.cols = 1
        self.invalid_injury.add_widget(Label(text = "Invalid input please use key words such as leg, arm or shoulder"))
        
        #injured area widgets
        self.injured_area.add_widget(Label(text="Injury Type: ", color = [46/255,128/255,28/255,1], font_size=32))
        # add Input Box
        self.injury = TextInput(multiline=False)
        self.injured_area.add_widget(self.injury)

        #add top grid
        self.add_widget(self.injured_area)

        #create a submit button
        self.submit = Button(text="Submit", font_size=32,
        size_hint_y = None,
        height = 50,
        background_normal = '',
        background_color = [250/255.0,1,1,1],
        color = [0,0,0,1]
        )
        #bind the button
        self.submit.bind(on_press=self.subm)
        #create button widget
        self.add_widget(self.submit)
    #submit instance ths calls the the exercises widget
    def subm(self, instance):
        injury = self.injury.text
        self.remove_widget(self.injured_area)
        self.remove_widget(self.submit)
        # print(f'Your injury is {injury}')
        #-removed- #self.exercises.add_widget(Label(text=f'Here are some exercises that your physical therapist has suggested for {injury}'))
        self.exercises.add_widget(Label(text=f'Here are some exercises that your physical therapist has suggested for {injury} injuries.'))
        #clear input boxes
        self.injury.text = ""
        #current injury options
        leg = "leg"
        arm = "arm" 
        shoulder = "shoulder"
        #injury option results
        if injury == leg:
            self.exercises.add_widget(self.leg_exercises)
        elif injury == shoulder:
            self.exercises.add_widget(self.shoulder_exercises)
        elif injury == arm:
            self.exercises.add_widget(self.arm_exercises)
        else:
            self.exercises.add_widget(self.invalid_injury)
        #build exercises widget
        self.add_widget(self.exercises)
        #creat back button
        self.back_to = Button(text="Go Back", font_size=32,
        size_hint_y = None,
        height = 50)
        #bind the button
        self.back_to.bind(on_press=self.backw)
        #create button widget
        self.add_widget(self.back_to)
        #Goes back to state original state
    def backw(self, instance):
        self.exercises.clear_widgets()
        self.clear_widgets()
        self.add_widget(self.injured_area)
        self.add_widget(self.submit)
        



class PhysTherApp(App):
    def build(self):
        #return Label(text="Welcome to Physical Therapy Guide")
         return MyGridLayout()

if __name__ == '__main__':
    PhysTherApp().run()