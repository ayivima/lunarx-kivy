import os

import kivy
kivy.require('1.0.7')
from kivy.app import App
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty


Config.set('graphics', 'resizable', False)


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Root(FloatLayout):
	loadfile = ObjectProperty(None)
	text_input = ObjectProperty(None)

	def dismiss_popup(self):
		self._popup.dismiss()

	def show_load(self):
		content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
		self._popup = Popup(title="Load Image", content=content,
							size_hint=(0.9, 0.9))
		self._popup.open()

	def load(self, path, filename):
		fname = os.path.join(path, filename[0])
		self.ids['newmessage'].opacity = 0
		for widg in ('rdetect', 'segm', 'rdetect_heading', 'segm_heading'):
			self.ids[widg].opacity = 1
		self.ids['rdetect'].source = 'outputs/largerock.png'
		self.ids['segm'].source = 'outputs/rockseg.png'
		self.dismiss_popup()


class LunarXApp(App):
	pass
		
Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)		

if __name__ == '__main__':
	LunarXApp().run()