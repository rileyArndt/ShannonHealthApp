from kivy.lang import Builder
from kivymd.app import MDApp



class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        return Builder.load_file('login.kv')
    
    def logger(self):
        import hashlib as hash
        from datetime import date
        import mysql.connector
        from mysql.connector import Error
        import geocoder
        import socket
        import datetime

        connection = mysql.connector.connect(host = "shannontestdatabase.cxc8luynmyvm.us-east-1.rds.amazonaws.com",
        user = "admin",
        passwd =  "mOBSCENE")
        print("Connection initialized")
        cursor = connection.cursor()
        cursor.execute("use shannon;")

        def grabQuery(query):
            connection = None 

            try:
                cursor.execute(query)
                ret = cursor.fetchall()
                print("Query successful")
            except Error as err:
                print(f"Error: '{err}'")
            return ret

        def insertQuery(query):
            try:
                cursor.execute(query)
                connection.commit()
                print("Query successful")
            except Error as err:
                print(f"Error: '{err}'")


        username = str(self.root.ids.user.text)
        while '@' not in username or '.' not in username:
            self.root.ids.warning_label.text = "please enter a valid email"
            return
        secret = str(self.root.ids.password.text)
        sal = grabQuery(""" 
        select sal from auth 
        where email = '""" + username +"';")
        if len(sal) > 0:
            sal = sal[0][0]
            secret = hash.md5((sal + secret).encode())   #placeholder
            secret = secret.hexdigest()
            if secret == grabQuery("select phash from auth where email='" + username + "';")[0][0]: 
                city = geocoder.ip("me").city
                realip = socket.gethostbyname(socket.gethostname())
                time = str(datetime.datetime.now())[:-7]
                insertQuery("update auth set location = '" + city + "', ip = '" + realip+"', logintime = '" + time + "' where email = '"+ username+ "';")
                print("Account Authorized")
            else:
                self.root.ids.warning_label.text = "Could not authenticate user, please re-enter your credentials."
                return
        else:
            self.root.ids.warning_label.text = "Could not authenticate user, please re-enter your credentials."
            return


    def create(self):
        print("test")

    def forgot(self):
        print("test")

MainApp().run()