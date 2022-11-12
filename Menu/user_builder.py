"""
User Authentification Functionality
"""

from str_builder import *

complete_app_builder += """
<Login>:
   name: 'login'
   Screen:
      MDBoxLayout:
         pos_hint: {"center_x": 0.5, "center_y": 0.5}
         padding: 25
         spacing: 25
         orientation: 'vertical'
         
         Image:
            source: 'Icons\ShannonLogo.png'
            pos_hint: {"center_x": 0.5}

         MDLabel:
            id: welcome_label
            text: "Login"
            font_size: 22
            halign:'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15

         MDTextField:
            id: user
            hint_text: "Email"
            icon_right: "account"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}


         MDTextField:
            id: password
            hint_text: "Password"
            icon_right: "eye-off"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}
            password: True

         MDLabel:
            id: warning_label
            text: " "
            font_size: 12
            halign:'center'
            size_hint_y: None
            height: self.texture_size[1]

         MDRoundFlatButton:
            text: "Log In"
            font_size: 20
            pos_hint: {"center_x": 0.5}
            on_press: app.logger()

         MDFlatButton:
            text: "Create account"
            font_size: 12
            pos_hint: {"center_x": 0.5}
            on_release: root.manager.current = "main"

         MDFlatButton:
            text: "Forgot Password"
            font_size: 10
            pos_hint: {"center_x": 0.5}
            on_press: root.manager.current = "forgot"





<Forgot>:
   name: 'forgot'
   Screen:
      MDBoxLayout:
         pos_hint: {"center_x": 0.5, "center_y": 0.5}
         padding: 25
         spacing: 25
         orientation: 'vertical'

         Image:
            source: 'Icons\ShannonLogo.png'
            pos_hint: {"center_x": 0.5}

         MDLabel:
            id: welcome_label
            text: "Enter email for authentication code"
            font_size: 22
            halign:'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15

         MDTextField:
            id: mail1
            hint_text: "Email"
            icon_right: "account"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}

         MDLabel:
            id: warning_label
            text: " "
            font_size: 12
            halign:'center'
            size_hint_y: None
            height: self.texture_size[1]

         MDRoundFlatButton:
            id:email
            text: "Send Confirmation Email"
            font_size: 20
            pos_hint: {"center_x": 0.5}
            on_press: app.forgot()

         MDFlatButton:
            text: "Go Back"
            font_size: 12
            pos_hint: {"center_x": 0.5}
            on_release: root.manager.current = "login"

            MDFlatButton:
               text: "-"
               font_size: 10
               pos_hint: {"center_x": 0.5}
               on_release: ''

<Forgot2>:
   name: 'forgot2'
   Screen:
      MDBoxLayout:
         pos_hint: {"center_x": 0.5, "center_y": 0.5}
         padding: 25
         spacing: 25
         orientation: 'vertical'
         
         Image:
            source: 'Icons\ShannonLogo.png'
            pos_hint: {"center_x": 0.5}

         MDLabel:
            id: welcome_label
            text: "We sent a code to the address entered. Please enter the code below."
            font_size: 22
            halign:'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15

         MDTextField:
            id: mail1
            hint_text: "code"
            icon_right: "account"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}

         MDLabel:
            id: warning_label
            text: " "
            font_size: 12
            halign:'center'
            size_hint_y: None
            height: self.texture_size[1]

            MDRoundFlatButton:
               id:email
               text: "Confirm Code"
               font_size: 20
               pos_hint: {"center_x": 0.5}
               on_press: app.forgot2()

            MDFlatButton:
               text: "Go Back"
               font_size: 12
               pos_hint: {"center_x": 0.5}
               on_release: root.manager.current = "login"

            MDFlatButton:
               text: "-"
               font_size: 10
               pos_hint: {"center_x": 0.5}
               on_release: ''

<Forgot3>:
   name: 'forgot3'
   Screen:
      MDBoxLayout:
         pos_hint: {"center_x": 0.5, "center_y": 0.5}
         padding: 25
         spacing: 25
         orientation: 'vertical'
         
         Image:
            source: 'Icons\ShannonLogo.png'
            pos_hint: {"center_x": 0.5}


         MDLabel:
            id: welcome_label
            text: "Enter Password"
            font_size: 28
            halign:'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15

         MDTextField:
            id: mail1
            hint_text: "Enter New Password"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}
            password: True

         MDTextField:
            id: mail2
            hint_text: "Confirm Password"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}
            password: True


         MDLabel:
            id: warning_label
            text: " "
            font_size: 12
            halign:'center'
            size_hint_y: None
            height: self.texture_size[1]

         MDRoundFlatButton:
            id:email
            text: "Change Password"
            font_size: 20
            pos_hint: {"center_x": 0.5}
            on_press: app.forgot3()

         MDFlatButton:
            text: "Go Back"
            font_size: 12
            pos_hint: {"center_x": 0.5}
            on_release: root.manager.current = "login"

         MDFlatButton:
            text: "-"
            font_size: 10
            pos_hint: {"center_x": 0.5}
            on_release: ''
             
    

<Create>:
   name: 'create'
   Screen:
      MDBoxLayout:
         pos_hint: {"center_x": 0.5, "center_y": 0.5}
         padding: 25
         spacing: 25
         orientation: 'vertical'
         
         Image:
            source: 'Icons\ShannonLogo.png'
            pos_hint: {"center_x": 0.5}


         MDLabel:
            id: welcome_label
            text: "Create Account"
            font_size: 30
            halign:'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15

         MDTextField:
            id: mail1
            hint_text: "Email"
            icon_right: "account"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}


         MDTextField:
            id: mail2
            hint_text: "Re-enter Email"
            #icon_right: "eye-off"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}

         MDLabel:
            id: warning_label
            text: " "
            font_size: 12
            halign:'center'
            size_hint_y: None
            height: self.texture_size[1]

         MDRoundFlatButton:
            text: "Validate Email"
            font_size: 20
            pos_hint: {"center_x": 0.5}
            on_press: app.create()

         MDFlatButton:
            text: "Go Back"
            font_size: 12
            pos_hint: {"center_x": 0.5}
            on_release: root.manager.current = "login"

         MDFlatButton:
            text: "-"
            font_size: 10
            pos_hint: {"center_x": 0.5}
            on_release: ''

<Create2>:
   name: 'create2'
   Screen:
      MDBoxLayout:
         pos_hint: {"center_x": 0.5, "center_y": 0.5}
         padding: 25
         spacing: 25
         orientation: 'vertical'
         
         Image:
            source: 'Icons\ShannonLogo.png'
            pos_hint: {"center_x": 0.5}

         
         MDLabel:
            id: welcome_label
            text: "Enter password for account"
            font_size: 25
            halign:'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15

         MDTextField:
            id: mail1
            hint_text: "Password"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}
            password: True


         MDTextField:
            id: mail2
            hint_text: "Re-enter Password"
            #icon_right: "eye-off"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}
            password: True

         MDLabel:
            id: warning_label
            text: " "
            font_size: 12
            halign:'center'
            size_hint_y: None
            height: self.texture_size[1]

         MDRoundFlatButton:
            text: "Create Account"
            font_size: 20
            pos_hint: {"center_x": 0.5}
            on_press: app.create2()

         MDFlatButton:
            text: "Go Back"
            font_size: 12
            pos_hint: {"center_x": 0.5}
            on_release: root.manager.current = "create"

         MDFlatButton:
            text: "-"
            font_size: 10
            pos_hint: {"center_x": 0.5}
            on_release: ''
"""
