#!/usr/bin/python

###################################################################
#This Class is used for first fit bin packing
#based on http://codeincomplete.com/posts/2011/5/7/bin_packing/
###################################################################
import binPackerObject
import blockObject

class binPacker(object):
	
	rootBinPackerObject = None
	
	#set up init where we set up the root object that all of the bin items live in
	#
	def __init__(self, passedWidth, passedHeight):
			self.rootBinPackerObject = binPackerObject.binPackerObject(passedWidth, passedHeight, 0, 0)
	
	#fit function: this function finds a fit for a passed in binPackerNode within the initial root, takes an array of items with 
	#width and height {width: N, height: N}
	#
	def fit(self, passedItemArray):
		node = None
		arrayItem = None
		
		#loop thru the passed array
		#
		for x in range(0,len(passedItemArray)):
			
			arrayItem = passedItemArray[x]
			
			#now lets see if we can fit this arrayItem into a node
			#
			node = self.findBinPackerNode(self.rootBinPackerObject, arrayItem.width, arrayItem.height)
			if(node is not None):
				arrayItem.fit = self.splitBinPackerNode(node, arrayItem.width, arrayItem.height)
		
	
	#find node function, searches for the root to place the item
	#
	def findBinPackerNode(self, passedRootBinPackerObject, passedWidth, passedHeight):
		
		#if we have already seen this root then check left and down
		#
		if(passedRootBinPackerObject.used):
			
			return self.findBinPackerNode(passedRootBinPackerObject.right, passedWidth, passedHeight) or self.findBinPackerNode(passedRootBinPackerObject.down, passedWidth, passedHeight)
		
		elif((passedWidth <= passedRootBinPackerObject.width) and (passedHeight <= passedRootBinPackerObject.height)):
			
			#ok we have a node we can add to
			#
			return passedRootBinPackerObject
		
		else:
			return None
	
	#split node function, this is the function that takes a node and places the arrayItem and then
	#splits the node into two new nodes (right and down)
	#
	def splitBinPackerNode(self, passedRootBinPackerObject, passedWidth, passedHeight):
		
		passedRootBinPackerObject.used = True
		
		#set up dem new objects
		#
		passedRootBinPackerObject.down =  binPackerObject.binPackerObject(passedRootBinPackerObject.width, passedRootBinPackerObject.height - passedHeight, passedRootBinPackerObject.x, passedRootBinPackerObject.y + passedHeight)
		
		passedRootBinPackerObject.right =  binPackerObject.binPackerObject(passedRootBinPackerObject.width - passedWidth, passedHeight, passedRootBinPackerObject.x + passedWidth, passedRootBinPackerObject.y)
		
		return passedRootBinPackerObject
		

	
	
	
	
	
	
	
	
	
	
	