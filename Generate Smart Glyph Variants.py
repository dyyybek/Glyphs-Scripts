#MenuTitle: Generate Smart Glyphs Variations
# -*- coding: utf-8 -*-
__doc__="""
Simple loop for generating smart glyphs. Feel free to modify to your needs.
"""

font = Glyphs.font
layer = font.selectedLayers[0]
glyph = layer.parent
currentGlyph = glyph.name
print currentGlyph

n = 100
for x in range(1,12):
	for y in range (1,12):
		n = n+1
		basename = "C."
		glifname = basename + str(n)
		del(font.glyphs[glifname])

n = 100
z = -10
for x in range(1,12):
	x = -10
	z = z+10
	for y in range (1,12):
		x = x+10
		n = n+1
		basename = "C."
		layer.components[0].smartComponentValues['Contrast'] = x
		layer.components[0].smartComponentValues['Buldge'] = z
		newglyph = font.glyphs[currentGlyph].copy()
		newglyph.name = basename + str(n)
		font.glyphs.append(newglyph)
		print x
