#!/usr/bin/python

###################################################################
#This Class is used for holding height and width
#based on http://codeincomplete.com/posts/2011/5/7/bin_packing/
###################################################################

class binPackerObject(object):
	
	width = 0
	height = 0
	x = 0
	y = 0
	
	used = False
	down = None
	right = None
	
	#init
	#
	def __init__(self, passedWidth, passedHeight, passedX, passedY):
		self.width = passedWidth
		self.height = passedHeight
		self.x = passedX
		self.y = passedY