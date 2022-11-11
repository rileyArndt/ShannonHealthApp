from kivy.core.window import Window
from kivy.uix.label import Label
from kivymd.uix.datatables import MDDataTable
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivy.lang.builder import Builder
from kivy.lang import Builder
from datetime import datetime
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.list import MDList, TwoLineListItem, ThreeLineIconListItem, TwoLineAvatarListItem,ThreeLineIconListItem, IconLeftWidget, OneLineListItem
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix import *
from kivymd.uix.textfield import MDTextField
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.recycleboxlayout import *
from kivy.uix.recycleview import RecycleView
#import mysql.connector
#import keyboard
from numpy import minimum
from kivy.uix.relativelayout import RelativeLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.graphics import Color, Canvas, Line, RoundedRectangle
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from threading import Event
#from kivy.properties import StringProperty, NumericProperty
from kivy.core.text import LabelBase
from kivy.clock import Clock
import webbrowser
import time
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import colors as mcolors, path
import datetime as dt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
#
#Builder.load_string("""
#<MenuScreen>:
#    BoxLayout:
#        orientation: 'vertical'
#        Button:
#            
#            border: (1,1,1,1)
#            background_normal: ''
#            background_color:(240/255, 240/255, 240/255, 1)
#            font_size:16
#            color:23/255, 135/255, 84/255, 1
#            size_hint:(1,.8)
#            text: 'Urgent Care Wait Times\\n\\n'+': '+'minutes\\n'+': '+'minutes\\n'
#            on_press:
#                root.manager.transition.direction = 'left'
#                root.manager.current = 'settings'
#        Button:
#            background_normal: ''
#            background_color:(240/255, 240/255, 240/255, 1)
#            font_size:16
#            size_hint:(1,.2)
#            color:23/255, 135/255, 84/255, 1
#            text: 'Back'
#            on_release:

#<SettingsScreen>:
#    BoxLayout:
#        orientation: 'vertical'
#        Button:
#            text: 'My settings button'
#            background_normal: ''
#            background_color:(240/255, 240/255, 240/255, 1)
#            font_size:16
#            color:23/255, 135/255, 84/255, 1
#            size_hint:(1,.8)
#        Button:
#            text: 'Back to menu'
#            background_normal: ''
#            background_color:(240/255, 240/255, 240/255, 1)
#            font_size:16
#            color:23/255, 135/255, 84/255, 1
#            size_hint:(1,.2)
#            on_press:
#                root.manager.transition.direction = 'right'
#                root.manager.current = 'menu'
#""")

# Declare both screens
#class MenuScreen(Screen):
#    pass

#class SettingsScreen(Screen):
#    pass

#class TestApp(App):

#    def build(self):
        # Create the screen manager
#        sm = ScreenManager()
#        sm.add_widget(MenuScreen(name='menu'))
#        sm.add_widget(SettingsScreen(name='settings'))
#
#        return sm


class dataAtView(App):

    def build_loc_string():
        a='Shannon Urgent Care Wait Times\n    '
        loc1=['test loc 1',23]
        loc2=['test loc 2',125]
        loc3=['test loc 3',2]
        locs=[loc1,loc2,loc3]

        for i in locs:
            a+=i[0]
            a+=': '
            a+=str(i[1])
            a+=' minutes\n    '
        return a

    def build(self):

        superBox= BoxLayout(orientation = 'vertical')
        horiz= BoxLayout(orientation='horizontal',padding = 1, spacing=2)
        horiz2=BoxLayout(orientation='horizontal',padding = 1, spacing=2)
        vert=BoxLayout(orientation = 'vertical',padding = 1)

        label_string = dataAtView.build_loc_string()


        #button for shannon wait times
        btn1 = Button(
            background_normal = '',
            text=label_string,
            font_size=22,
            size_hint=(.7,1),
            background_color = (240/255, 240/255, 240/255, 1),
            color = (23/255, 135/255, 84/255, 1),
        )

        btn2 = Button(
           background_normal = '',
            text='test\ntestName: testTime\ntestName: testTime\ntestName: testTime',
            font_size=22,
            size_hint=(.7,1),
            background_color = (240/255, 240/255, 240/255, 1),
            color = (23/255, 135/255, 84/255, 1),
        )
        horiz.add_widget(btn1)
        horiz.add_widget(btn2)

        
        btn4 = Button(
            background_normal = '',
            text=label_string,
            font_size=22,
            size_hint=(.7,1),
            background_color = (240/255, 240/255, 240/255, 1),
            color = (23/255, 135/255, 84/255, 1),
        )

        btn5 = Button(
           background_normal = '',
            text='test\ntestName: testTime\ntestName: testTime\ntestName: testTime',
            font_size=22,
            size_hint=(.7,1),
            background_color = (240/255, 240/255, 240/255, 1),
            color = (23/255, 135/255, 84/255, 1), 
        )
        horiz2.add_widget(btn4)
        horiz2.add_widget(btn5)

        btn3 = Button(
            background_normal = '',
            text='Quit',
            font_size=22,
            size_hint=(1,.1),
            background_color = (240/255, 240/255, 240/255, 1),
            color = (23/255, 135/255, 84/255, 1),
            border=(16,16,16,16) 
        )

        vert.add_widget(btn3)

        vert.size_hint = (1,.4)
        superBox.add_widget(horiz)
        superBox.add_widget(horiz2)
        superBox.add_widget(vert)

        return superBox
    

if __name__ == '__main__':
    dataAtView().run()
