from BinaryTree import BinaryTree 
from BTreeNode import BTreeNode
import math

#set up binary tree
#

node1 = BTreeNode(12,None, None)
node2 = BTreeNode(13,None, None)
node3 = BTreeNode(11,None, None)
node4 = BTreeNode(10,None, None)
 
tree = BinaryTree(node1)

tree.addNewNode(node2)
tree.addNewNode(node3)
tree.addNewNode(node4)

print 'Node Count ' + str(tree.nodeCount)
print 'Height ' + str(tree.getHeight())
print tree.findNodeAndParent(11, tree.rootNode)
list = tree.findNodeAndParent(11, tree.rootNode)

print 'Getting info out of the List'
print list[0].getInformation()
print list[1].getInformation()
print '=========================================='

tree.recursiveInOrderBinaryTreeLoop(tree.rootNode)

print '=========================================='

tree.recursivePreOrderBinaryTreeLoop(tree.rootNode)

print '=========================================='

tree.recursivePostOrderBinaryTreeLoop(tree.rootNode)