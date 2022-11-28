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

        self.mapview = MapView(zoom = 12, lat = 31.4638, lon = -100.4370)
        self.mapview.double_tap_zoom = True

        # Shannon Medical Center
        self.marker1 = MapMarkerPopup()
        self.marker1.lat = 31.465321
        self.marker1.lon = -100.434753
        # Shannon Medical Center
        self.mapview.add_widget(self.marker1)

        self.medbtn1 = Button()
        self.medbtn1.text = "Shannon Medical Center"
        self.medbtn1.size_hint = [ 2, 0.5 ]

        self.marker1.add_widget(self.medbtn1)
        # Centers map on marker clicked.
        self.marker1.bind(on_press = lambda x: self.mapview.center_on(self.marker1.lat, self.marker1.lon))

        # Shannon Clinic
        self.marker2 = MapMarkerPopup()
        self.marker2.lat = 31.426300
        self.marker2.lon = -100.495770
        # Shannon Clinic
        self.mapview.add_widget(self.marker2)

        self.medbtn2 = Button()
        self.medbtn2.text = "Shannon Clinic"
        self.medbtn2.size_hint = [ 2, 0.5 ]
        self.marker2.add_widget(self.medbtn2)
        # Centers map on marker clicked.
        self.marker2.bind(on_press = lambda x: self.mapview.center_on(self.marker2.lat, self.marker2.lon))

        # Shannon Urgent Care West
        self.marker3 = MapMarkerPopup()
        self.marker3.lat = 31.432950
        self.marker3.lon = -100.500710
        # Urgent Care West
        self.mapview.add_widget(self.marker3)

        self.medbtn3 = Button()
        self.medbtn3.text = "Shannon Urgent Care West"
        self.medbtn3.size_hint = [ 2, 0.5 ]
        self.marker3.add_widget(self.medbtn3)
        # Centers map on marker clicked.
        self.marker3.bind(on_press = lambda x: self.mapview.center_on(self.marker3.lat, self.marker3.lon))

        # Shannon South Hospital
        self.marker4 = MapMarkerPopup()
        self.marker4.lat = 31.418409
        self.marker4.lon = -100.469887
        # South Hospital
        self.mapview.add_widget(self.marker4)

        self.medbtn4 = Button()
        self.medbtn4.text = "Shannon South Hospital"
        self.medbtn4.size_hint = [ 2, 0.5 ]
        self.marker4.add_widget(self.medbtn4)

        # Shannon Senior Health Center
        self.marker5 = MapMarkerPopup()
        self.marker5.lat = 31.429410
        self.marker5.lon = -100.478960
        # Senior Health Center
        self.mapview.add_widget(self.marker5)

        self.medbtn5 = Button()
        self.medbtn5.text = "Shannon Senior Health-Center"
        self.medbtn5.size_hint = [ 2, 0.5 ]
        self.marker5.add_widget(self.medbtn5)

        # Shannon Clinic South
        self.marker6 = MapMarkerPopup()
        self.marker6.lat = 31.419360
        self.marker6.lon = -100.468500
        # Clinic South
        self.mapview.add_widget(self.marker6)

        self.medbtn6 = Button()
        self.medbtn6.text = "Shannon Clinic South"
        self.medbtn6.size_hint = [ 2, 0.5 ]
        self.marker6.add_widget(self.medbtn6)

        # Shannon Clinic South-West
        self.marker7 = MapMarkerPopup()
        self.marker7.lat = 31.436040
        self.marker7.lon = -100.501920
        # Clinic South-West
        self.mapview.add_widget(self.marker7)

        self.medbtn7 = Button()
        self.medbtn7.text = "Shannon Clinic South-West"
        self.medbtn7.size_hint = [ 2, 0.5 ]
        self.marker7.add_widget(self.medbtn7)

        # Shannon Clinic
        self.marker8 = MapMarkerPopup()
        self.marker8.lat = 31.463770
        self.marker8.lon = -100.434174
        # Clinic
        self.mapview.add_widget(self.marker8)

        self.medbtn8 = Button()
        self.medbtn8.text = "Shannon Clinic"
        self.medbtn8.size_hint = [ 2, 0.5 ]
        self.marker8.add_widget(self.medbtn8)

        # Shannon Urgent Care South
        self.marker9 = MapMarkerPopup()
        self.marker9.lat = 31.420220
        self.marker9.lon = -100.470690
        # Urgent Care South
        self.mapview.add_widget(self.marker9)

        self.medbtn9 = Button()
        self.medbtn9.text = "Shannon Urgent Care South"
        self.medbtn9.size_hint = [ 2, 0.5 ]
        self.marker9.add_widget(self.medbtn9)

        # Shannon Health Club
        self.marker10 = MapMarkerPopup()
        self.marker10.lat = 31.420150
        self.marker10.lon = -100.480310
        # Health Club
        self.mapview.add_widget(self.marker10)

        self.medbtn10 = Button()
        self.medbtn10.text = "Shannon Health Club"
        self.medbtn10.size_hint = [ 2, 0.5 ]
        self.marker10.add_widget(self.medbtn10)

        # Shannon Clinic Jackson
        self.marker11 = MapMarkerPopup()
        self.marker11.lat = 31.436550
        self.marker11.lon = -100.457060
        # Clinic Jackson
        self.mapview.add_widget(self.marker11)

        self.medbtn11 = Button()
        self.medbtn11.text = "Shannon Clinic Jackson"
        self.medbtn11.size_hint = [ 2, 0.5 ]
        self.marker11.add_widget(self.medbtn11)

        # Shannon Business Office
        self.marker12 = MapMarkerPopup()
        self.marker12.lat = 31.468750
        self.marker12.lon = -100.431220
        # Business Office
        self.mapview.add_widget(self.marker12)

        self.medbtn12 = Button()
        self.medbtn12.text = "Shannon Business Office"
        self.medbtn12.size_hint = [ 2, 0.5 ]
        self.marker12.add_widget(self.medbtn12)

        self.btn = MDRectangleFlatButton(_default_text_color=(23/255, 135/255, 84/255, 0))
        #self.btn.set_text_color(23/255, 135/255, 84/255, 1)
        self.btn.text = "Click Me"
        self.btn.halign = "center"
        self.btn.bind(on_press = self.openMC)

        self.lout.add_widget(self.mapview)
        self.lout.add_widget(self.btn)

        self.add_widget(self.lout)

    def openMC(self, instance):
        import webbrowser
        webbrowser.open('https://www.shannonhealth.com/locations.aspx')

class MapViewApp(MDApp):
    def build(self):
        return MapScreen() 
    pass

MapViewApp().run()
