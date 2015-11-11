#MenuTitle: Import Images by Unicode Code Point
# -*- coding: utf-8 -*-
__doc__="""
Imports images pre-named with unicode code point or glyph names into a coresponding Glyph and currently selected Master.
"""

import GlyphsApp
from vanilla import *

class EditTextDemo(object):

	def __init__(self):
		self.w = Window((800, 200), title="Import Many Images")
		self.w.box = Box((10, 45, -210, 60))
		self.w.box2 = Box((600, 45, -10, 60))
		self.w.instruction = TextBox((10, 10, -10, 22), text="Please specify image naming scheme, image extension, path to images.")
		self.w.path = TextBox((10, 115, -10, 22))
		self.w.line2 = HorizontalLine((10, 35, -10, 1))
		self.w.box2.extensiontext = TextBox((10, 0, -10, 22), text="Extension")
		self.w.box2.extension = EditText((10, 20, 130, 22), placeholder=".jpeg")
		self.w.pickPath = Button((10, 140, -10, 20), "Choose Path to Images", callback=self.pickPath)
		self.w.testButton = Button((10, 170, -10, 20), "Run Script", callback=self.placeImages)
		self.w.box.method = RadioGroup((10, 5, -10, 40),
                                ["By Unicode Code Point [00E4]", "By Glyph Name [adieresis]"])
		
		self.w.open()
        
	def pickPath(self, sender):
		pickpath = GetFolder("Please choose a folder with images") + '/'
		self.w.path.set(pickpath)
		
	def buttonshit(self, sender):
		self.buttonCallback(self)
	
	def placeImages(self,sender):
		pickpath = self.w.path.get()
		pickmethod = self.w.box.method.get()
		pickextension = self.w.box2.extension.get()
		
			
		masterID = Glyphs.font.masters[Glyphs.font.masterIndex].id
		for glyph in Glyphs.font.glyphs:
			if pickmethod == 0:
				if glyph.unicode:
					layer = glyph.layers[masterID]
					layer.backgroundImage = GSBackgroundImage(pickpath + glyph.unicode + pickextension)
			if pickmethod == 1:
				if glyph.name:
					layer = glyph.layers[masterID]
					layer.backgroundImage = GSBackgroundImage(pickpath + glyph.name + pickextension)
				
EditTextDemo()