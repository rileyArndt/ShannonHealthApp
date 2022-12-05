from main import *


        
# Identifies the client's injury
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
        self.leg_exercises.add_widget(Label(text = "Leg Raises", font_size =32, color=[46/255,128/255,28/255,1]))
        self.leg_exercises.add_widget(Label(text = "Leg Stretches", font_size =32, color=[46/255,128/255,28/255,1]))
        self.leg_exercises.add_widget(Label(text = "Lying Hamstring Stretch", font_size =32, color=[46/255,128/255,28/255,1]))
        self.leg_exercises.add_widget(Label(text = "Quadriceps Stretch", font_size =32, color=[46/255,128/255,28/255,1]))
        self.leg_exercises.add_widget(Label(text = "Calf Stretches", font_size =32, color=[46/255,128/255,28/255,1]))
        
        #arm
        self.arm_exercises = GridLayout()
        self.arm_exercises.cols = 2
        self.arm_exercises.add_widget(Label(text = "Crossover Arm Stretch", font_size =32, color=[46/255,128/255,28/255,1]))
        self.arm_exercises.add_widget(Label(text = "Doorway Stretch", font_size =32, color=[46/255,128/255,28/255,1]))
        self.arm_exercises.add_widget(Label(text = "Lawn Mower Pull", font_size =32, color=[46/255,128/255,28/255,1]))
        self.arm_exercises.add_widget(Label(text = "Reverse Fly", font_size =32, color=[46/255,128/255,28/255,1]))
        self.arm_exercises.add_widget(Label(text = "Arm Exercise 5", font_size =32, color=[46/255,128/255,28/255,1]))
        
        #shoulder
        self.shoulder_exercises = GridLayout()
        self.shoulder_exercises.cols = 2
        self.shoulder_exercises.add_widget(Label(text = "Neck Release", font_size =32, color=[46/255,128/255,28/255,1]))
        self.shoulder_exercises.add_widget(Label(text = "External Rotation", font_size =32, color=[46/255,128/255,28/255,1]))
        self.shoulder_exercises.add_widget(Label(text = "Elbow Flex", font_size =32, color=[46/255,128/255,28/255,1]))
        self.shoulder_exercises.add_widget(Label(text = "Chest Expansion", font_size =32, color=[46/255,128/255,28/255,1]))
        self.shoulder_exercises.add_widget(Label(text = "Eagle Pose", font_size =32, color=[46/255,128/255,28/255,1]))
        #invalid input
        self.invalid_injury = GridLayout()
        self.invalid_injury.cols = 1
        self.invalid_injury.add_widget(Label(text = "Invalid input \nplease use key words such as leg, arm or shoulder", color=[46/255,128/255,28/255,1]))
        
        #injured area widgets
        self.injured_area.add_widget(Label(text="Injury Type: ", color=[46/255,128/255,28/255,1], font_size=32))
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
        background_color = [46/255,128/255,28/255,1],
        color = [1,1,1,1]
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
        self.exercises.add_widget(Label(text=f'Here are some exercises that your \nphysical therapist has suggested for {injury} injuries.', color=[46/255,128/255,28/255,1]))
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
        
# Physical_Screen - Invovles identification of injuries.
class Physical_Screen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
    def on_enter(self, *args):
        self.clear_widgets()
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