#MenuTitle: Width Plus 20
# -*- coding: utf-8 -*-
__doc__="""
Simple script for changing width to current glyph. Assign a shortcut in system preferences.
"""

font = Glyphs.font
layer = font.selectedLayers[0]
width = layer.width
layer.width = width + 20
