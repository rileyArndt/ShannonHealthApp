from keyboard import on_release
from kivy.app import App
from kivy_garden.mapview import MapView
from kivy_garden.mapview import MapMarkerPopup
from kivy.uix.button import Button
from numpy import double

class MapViewApp(App):
    def build(self):
        mapview = MapView(zoom = 10, lat = 31.4638, lon = -100.4370)
        mapview.double_tap_zoom = True
        marker = MapMarkerPopup(lat = 31.4652, lon = -100.4344)
        marker.add_widget(Button(text = "Shannon"))
        mapview.add_widget(marker)


        return mapview 
    pass

MapViewApp().run()
