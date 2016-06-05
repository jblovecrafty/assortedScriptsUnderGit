#Binary Tree Class
#
import BTreeNode
import math

class BinaryTree():

	#set up init function
	#
	def __init__(self, passedRootNode):
		
		self.rootNode = passedRootNode
		self.nodeCount =  1

	#add nodes
	#gist of method is to start from root and compare information going either left or right depending on comparison value
	#
	def addNewNode(self, passedNewNode):
		
		#currentTestNode (we test the passed node against this)
		#if no root set then the add is easy otherwise set root node to current
		#
		if(self.rootNode is None):
			self.rootNode = passedNewNode
			self.nodeCount = 1
			return
		else:
			currentTestNode = self.rootNode
			
		#set up a boolean that tells us how long we need to loop for
		#
		isNewNodePlaceFound = False
		
		#now loop thru our binary tree to figure out where to add this new node
		#
		while(isNewNodePlaceFound != True):
			
			#compare those nodes first left then right
			#
			if(passedNewNode.information <= currentTestNode.information):
				
				 
				if(currentTestNode.getLeftNode() is None ):
					#added new node
					#
					self.nodeCount += 1
					currentTestNode.setLeftNode(passedNewNode)
					isNewNodePlaceFound = True
					return
					
				else:
					currentTestNode = currentTestNode.getLeftNode()
					
			
			else:
					
				 
				if(currentTestNode.getRightNode() is None ):
					#added new node
					#
					self.nodeCount+= 1
					currentTestNode.setRightNode(passedNewNode)
					isNewNodePlaceFound = True
					return
				else:
					currentTestNode = currentTestNode.getRightNode()
		
	
	#	
	#set up function to recursively count all the nodes
	#
	#function recursively and iteratively loop thru nodes
	#
	
	#recursive section
	#
	
	#in order b tree traversal
	#
	def recursiveInOrderBinaryTreeLoop(self, passedNode):
		
		if(passedNode is None):
			return
					
		#start with left node recursion
		#
		self.recursiveInOrderBinaryTreeLoop(passedNode.getLeftNode())
		
		#then print current node value
		# 
		print passedNode.getInformation()
		
		#then recurse thru right node
		#
		self.recursiveInOrderBinaryTreeLoop(passedNode.getRightNode())
		

	#pre order b tree traversal
	#
	def recursivePreOrderBinaryTreeLoop(self, passedNode):

		if(passedNode is None):
			return

		#then print current node value
		# 
		print passedNode.getInformation()
		
		#start with left node recursion
		#
		self.recursiveInOrderBinaryTreeLoop(passedNode.getLeftNode())

		#then recurse thru right node
		#
		self.recursiveInOrderBinaryTreeLoop(passedNode.getRightNode())
		
	
	#post order b tree traversal
	#
	def recursivePostOrderBinaryTreeLoop(self, passedNode):

		if(passedNode is None):
			return

		#start with left node recursion
		#
		self.recursiveInOrderBinaryTreeLoop(passedNode.getLeftNode())

		#then recurse thru right node
		#
		self.recursiveInOrderBinaryTreeLoop(passedNode.getRightNode())
		
		#then print current node value
		# 
		print passedNode.getInformation()
		
	
	#search for node and parent node
	#
	def findNodeAndParent(self, passedInformation, passedParentNode):
		
		#ok we are tapped out
		#
		if(passedParentNode is None):
			return
		
		#check if it is the root node
		#	
		if(self.rootNode.getInformation() == passedInformation):
			return self.rootNode
		
		valueList = []
		#do we have it?
		#check the left node
		#
		if(passedParentNode.getLeftNode().getInformation() == passedInformation):
			valueList.append(passedParentNode)
			valueList.append(passedParentNode.getLeftNode())
			return valueList
		
		#check the right node
		#	
		if(passedParentNode.getRightNode().getInformation() == passedInformation):
			valueList.append(passedParentNode)
			valueList.append(passedParentNode.getRightNode())
			return valueList
				
		
		#ok lets check the parent nodes left node and its right node
		#
		findNodeAndParent(passedInformation, passedParentNode.getLeftNode())
		findNodeAndParent(passedInformation, passedParentNode.getRightNode())
		
			
	
	#delete functionality
	#
	def deleteNodeWithValue(self, passedValue):
		#find the parent node and the node in question starting at the root
		#
		findNodeAndParent(self, passedInformation, passedParentNode):
		
		#ok if the node has no left or right trees just delete it and remove the refernce from the parent object
		#
		
		#if there is only one sub tree then link the sub tree to the parent node set the node to null
		#
		
		
		
		
	
	#height functionality
	#
	def getHeight(self):
		height = math.log(self.nodeCount+1)
		return height
		