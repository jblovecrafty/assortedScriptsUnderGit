#class for the node objects that will be used for binary trees
#
class BTreeNode():
	
	#set up init function
	#
	def __init__(self, passedInfomation, passedLeftNode, passedRightNode):
		
		#holds our information the rest are references to other nodes
		#
		self.information 	= passedInfomation
		self.leftNode 		= passedLeftNode
		self.rightNode	 	=  passedRightNode
		
	
	#get Information
	#
	def getInformation(self):
		return self.information
	
	#set Information
	#	
	def setInformation(self, passedInformation):
		self.information = passedInfomation

	#get LeftNode
	#
	def getLeftNode(self):
		return self.leftNode

	#set LeftNode
	#	
	def setLeftNode(self, passedLeftNode):
		self.leftNode = passedLeftNode
	
			
	#get RightNode
	#
	def getRightNode(self):
		return self.rightNode

	#set RightNode
	#	
	def setRightNode(self, passedRightNode):
		self.rightNode =  passedRightNode
		
		
		
		
