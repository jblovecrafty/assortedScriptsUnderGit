#!/usr/bin/python

###################################################################
#This Class is used for holding the node object
#based on http://codeincomplete.com/posts/2011/5/7/bin_packing/
###################################################################

class binPackerNode(object):
	
	used = False
	down = None
	right = None
	
	#init
	#
	def __init__(self):