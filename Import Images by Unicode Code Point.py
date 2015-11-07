#MenuTitle: Import Images by Unicode Code Point
# -*- coding: utf-8 -*-
__doc__="""
Imports images pre-named with unicode code point into a coresponding Glyph and currently selected Master
"""
import GlyphsApp

pickpath = GetFolder("Please choose a folder with images") + '/'
pickextension = 'png'
masterID = Glyphs.font.masters[Glyphs.font.masterIndex].id
for glyph in Glyphs.font.glyphs:
	if glyph.unicode:
		print glyph.unicode
		layer = glyph.layers[masterID]
		layer.backgroundImage = GSBackgroundImage(pickpath + glyph.unicode + '.' + pickextension)