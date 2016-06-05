#!/usr/bin/python
import binPacker
import binPackerObject
import blockObject
from Tkinter import *
from random import randint

#this is the test script for the binPacker and block object
#

block1 = blockObject.blockObject(20, 20)
block2 = blockObject.blockObject(20, 20)
block3 = blockObject.blockObject(20, 20)
block4 = blockObject.blockObject(20, 20)

print '======================================================='
print 'block object test'

print block1.width
print block1.height

print '======================================================='

print '======================================================='
print 'binPacker object test'
binPackObj1 = binPackerObject.binPackerObject(1, 5, 200, 300)
binPackObj2 = binPackerObject.binPackerObject(2, 5, 200, 300)
binPackObj3 = binPackerObject.binPackerObject(3, 5, 200, 300)

binPackObj1.left = binPackObj2
binPackObj1.down = binPackObj3

print binPackObj1.width
print binPackObj1.height
print binPackObj1.x
print binPackObj1.y

print binPackObj1.left.width
print binPackObj1.down.width
print '======================================================='

print '======================================================='
print 'block object list test'

listOfBlocks = [block1, block2, block3, block4]

for x in range(len(listOfBlocks)):
	print listOfBlocks[x].width

print '======================================================='

print '======================================================='
print 'bin packer test'

binPackerObj = binPacker.binPacker(40, 40)
binPackerObj.fit(listOfBlocks)

for x in range(len(listOfBlocks)):
	print 'X Location: ' + str(listOfBlocks[x].fit.x )
	print 'Y Location: ' + str(listOfBlocks[x].fit.y)


print '======================================================='


#list of colors
#
listOfColors = ['#e8d174','#e39e54','#d64d4d','#4d7358','#9ed670']

#draw items
#
master = Tk()
w = Canvas(master, width=200, height=100)
w.pack()              
 
for x in range(len(listOfBlocks)):    
	colorNum = randint(0,4) 
	print 'X Location: ' + str(listOfBlocks[x].fit.x)
	print 'Y Location: ' + str(listOfBlocks[x].fit.y)
	w.create_rectangle(listOfBlocks[x].fit.x, listOfBlocks[x].fit.y, (listOfBlocks[x].fit.x+listOfBlocks[x].width), (listOfBlocks[x].fit.y+listOfBlocks[x].height), fill=listOfColors[colorNum], width=1,outline='black')
	
	
mainloop()








