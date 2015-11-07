#MenuTitle: Import Images by Unicode Code Point
# -*- coding: utf-8 -*-
__doc__="""
Imports images pre-named with unicode code point into a coresponding Glyph and Master
"""

picklayer = 'Light Italic'
pickpath = '/Users/dyb/Desktop/'
pickextension = 'png'
masterID = None
for master in Glyphs.font.masters:
    if master.name == picklayer:
        masterID = master.id
for glyph in Glyphs.font.glyphs:
    if glyph.unicode:
        print glyph.unicode
        layer = glyph.layers[masterID]
        layer.backgroundImage = GSBackgroundImage(pickpath + glyph.unicode + '.' + pickextension)