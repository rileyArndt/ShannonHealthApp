#: kivy!
from keyboard import on_release
from kivymd.app import MDApp
from mymods import *
from kivy_garden.mapview import MapView
from kivy_garden.mapview import MapMarkerPopup
from kivy.uix.button import Button
from numpy import double

class MapScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # lout is the layout
        self.lout = BoxLayout()
        self.lout.orientation = "vertical"


        self.mapview = MapView(zoom = 10, lat = 31.4638, lon = -100.4370)
        self.mapview.double_tap_zoom = True

        # Shannon Medical Center
        self.marker1 = MapMarkerPopup()
        self.marker1.lat = 31.465321
        self.marker1.lon = -100.434753

        # Shannon Clinic
        self.marker2 = MapMarkerPopup()
        self.marker2.lat = 31.426300
        self.marker2.lon = -100.495770

        # Shannon Urgent Care West
        self.marker3 = MapMarkerPopup()
        self.marker3.lat = 31.432950
        self.marker3.lon = -100.500710

        # Shannon South Hospital
        self.marker4 = MapMarkerPopup()
        self.marker4.lat = 31.418409
        self.marker4.lon = -100.469887

        # Shannon Senior Health Center
        self.marker5 = MapMarkerPopup()
        self.marker5.lat = 31.429410
        self.marker5.lon = -100.478960

        # Shannon Clinic South
        self.marker6 = MapMarkerPopup()
        self.marker6.lat = 31.419360
        self.marker6.lon = -100.468500

        # Shannon Clinic South-West
        self.marker7 = MapMarkerPopup()
        self.marker7.lat = 31.436040
        self.marker7.lon = -100.501920

        # Shannon Clinic
        self.marker8 = MapMarkerPopup()
        self.marker8.lat = 31.463770
        self.marker8.lon = -100.434174

        # Shannon Urgent Care South
        self.marker9 = MapMarkerPopup()
        self.marker9.lat = 31.420220
        self.marker9.lon = -100.470690

        # Shannon Health Club
        self.marker10 = MapMarkerPopup()
        self.marker10.lat = 31.420150
        self.marker10.lon = -100.480310

        # Shannon Clinic Jackson
        self.marker11 = MapMarkerPopup()
        self.marker11.lat = 31.436550
        self.marker11.lon = -100.457060

        # Shannon Business Office
        self.marker12 = MapMarkerPopup()
        self.marker12.lat = 31.468750
        self.marker12.lon = -100.431220

        # 
        self.marker1.bind(on_press = self.change_zoom)
        # self.marker2.bind(on_press = self.change_zoom)
        # self.marker3.bind(on_press = self.change_zoom)

        self.medbtn = Button()
        self.medbtn.text = "Shannon Medical Center"
        self.medbtn.size_hint = [ 2, 0.5 ]

        self.marker1.add_widget(self.medbtn)

        # Shannon Medical Center
        self.mapview.add_widget(self.marker1)
        # Shannon Clinic
        self.mapview.add_widget(self.marker2)
        # Urgent Care West
        self.mapview.add_widget(self.marker3)
        # South Hospital
        self.mapview.add_widget(self.marker4)
        # Senior Health Center
        self.mapview.add_widget(self.marker5)
        # Clinic South
        self.mapview.add_widget(self.marker6)
        # Clinic South-West
        self.mapview.add_widget(self.marker7)
        # Clinic
        self.mapview.add_widget(self.marker8)
        # Urgent Care South
        self.mapview.add_widget(self.marker9)
        # Health Club
        self.mapview.add_widget(self.marker10)
        # Clinic Jackson
        self.mapview.add_widget(self.marker11)
        # Business Office
        self.mapview.add_widget(self.marker12)

        self.btn = MDRectangleFlatButton()
        self.btn.text = "Click Me"
        self.btn.halign = "center"
        self.btn.bind(on_press=self.react)

        self.lout.add_widget(self.mapview)
        self.lout.add_widget(self.btn)

        self.add_widget(self.lout)
    
    def react(self, obj):
        print("wut")

    def change_zoom(self, obj):
        self.mapview.zoom = 15
        self.mapview.center_on



class MapViewApp(MDApp):
    def build(self):
        return MapScreen() 
    pass

MapViewApp().run()
