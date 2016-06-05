#!/usr/bin/python
import binPackerObject

###################################################################
#This Class is used for holding height and width of an item
#based on http://codeincomplete.com/posts/2011/5/7/bin_packing/
###################################################################

class blockObject(object):
	
	width = 0
	height = 0
	word = None
	fit = None
	story = None
	
	#init
	#
	def __init__(self, passedWidth, passedHeight):
	        self.width = passedWidth
	        self.height = passedHeight