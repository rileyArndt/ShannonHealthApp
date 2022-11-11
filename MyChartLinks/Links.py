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





class TestApp(App):

    def build(self):
        self.window = BoxLayout(orientation = 'vertical', padding = 2, spacing = 2)

        self.button = Button(text="Call Provider",
            size_hint=(1,.8),
            background_normal = '',
            font_size = 22,
            background_color = (240/255, 240/255, 240/255, 1),
            color = (23/255, 135/255, 84/255, 1)
            )
        self.button.bind(on_press=self.openMC)
        self.window.add_widget(self.button)

        self.button = Button(text="Call Shannon",
            size_hint = (1,.8),
            background_normal = '',
            font_size = 22,
            background_color = (240/255, 240/255, 240/255, 1),
            color = (23/255, 135/255, 84/255, 1)
            )
        self.button.bind(on_press=self.openShannon)
        self.window.add_widget(self.button)

        self.button = Button(text="Shannon Telemed",
            size_hint = (1,.8),
            background_normal = '',
            font_size = 22,
            background_color = (240/255, 240/255, 240/255, 1),
            color = (23/255, 135/255, 84/255, 1)
            )
        self.button.bind(on_press=self.openShannon)
        self.window.add_widget(self.button)

        self.button=Button(text="Back",
            size_hint=(1,.3),
            background_normal = '',
            font_size = 22,
            background_color = (240/255, 240/255, 240/255, 1),
            color = (23/255, 135/255, 84/255, 1)
            
            )
        self.window.add_widget(self.button)

        return self.window

    def openMC(self, instance):
        import webbrowser
        webbrowser.open('https://www.mychart.com/')

    def openShannon(self, instance):
        import webbrowser
        webbrowser.open('https://www.shannonhealth.com/')

        

if __name__ == '__main__':
    TestApp().run()
