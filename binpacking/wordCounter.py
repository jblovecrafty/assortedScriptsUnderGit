#!/usr/bin/python
import fileinput
from operator import itemgetter
import binPacker
import binPackerObject
import blockObject
import math
import json
from Tkinter import *
from random import randint


###################################################################
#count the number of different words (and which are they)
###################################################################

#list of common words
#
commonWordList = ['the','be','to','of','and','a','in','that','have','i','it','for','not','on','with','he','as','you','do','at','this','but','his','by','from','they','we','say','her','she','or','an','will','my','one','all','would','there','their','what','so','up','out','if','about','who','get','which','go','me','when','make','can','like','time','no','just','him','know','take','person','into','year','your','good','some','could','them','see','other','than','then','now','look','only','come','its','over','think','also','back','after','use','two','how','our','work','first','well','way','even','new','want','because','any','these','give','day','most','us', 'was','-','...', 'had']


#this parses out words in a text files and groups them
#
def wordParser(passedFileHandleLocation, passedExistingDict):

	fileHandle = open(passedFileHandleLocation, "r")
	
	#init dictionary with word and count
	#
	wordCountDict = passedExistingDict
	
	#read file into var
	#each line increment word or add new word and add one
	#
	for line in fileHandle:
	
		wordTuple = line.split()
	
		for word in wordTuple:
			
			#string cleaning
			#
			word = word.lower()
			word = word.translate(None, ",!.;'")
		
			#filter out common words
			#
			if(not word in commonWordList):

				if(word in wordCountDict):
					wordCountDict[word] = wordCountDict[word]+1
				else:
					wordCountDict[word] = 1

	#close file
	#	
	fileHandle.close()
					
	return wordCountDict

#builds a sorted list of words based on number
#
def buildSortedBinList(passedDictToBeSorted,passedTotalArea, passedMaxNumberOfWords, passedIsAllWords, passedAddToSize):
	sortedList = sorted(passedDictToBeSorted.items(), key=itemgetter(1), reverse=True)

	for keyWord, numberOfTimes in sortedList:	
   		#print "word:" + keyWord + " number:" + str(numberOfTimes) + " " + ('.' * numberOfTimes)


		#handle the bin packing algorithm
		#
		sortedBlockList = []
		totalArea = passedTotalArea

		#the number of words we are interested in seeing
		#
		numberOfWords = passedMaxNumberOfWords
		wordsCounted = 0
		isAllWords = passedIsAllWords

		#area additive for size
		#
		addToSize = passedAddToSize

		#build sorted list
		#
		for keyWord, numberOfTimes in sortedList:
	
			if(passedIsAllWords):
				blockObj = blockObject.blockObject(numberOfTimes+addToSize, numberOfTimes+addToSize)
				blockObj.word = keyWord
				#blockObj.story = passedWordSource;
				sortedBlockList.append(blockObj)
			else:
				if(wordsCounted <= numberOfWords):
					wordsCounted += 1
					#print "words counted"
					#print wordsCounted
			
					blockObj = blockObject.blockObject(numberOfTimes+addToSize, numberOfTimes+addToSize)
					blockObj.word = keyWord
					#blockObj.story = passedWordSource;
					sortedBlockList.append(blockObj)
					
	return sortedBlockList	

#build area of root
#
def buildPackedBin(passedSortedBlockList, passedAreaAdditive):
	
	totalPackArea = 0
	
	for x in passedSortedBlockList:
	
		print "word:" + x.word + " x: " + str(x.width * x.height )
		totalPackArea += (x.width * x.height)
		

	totalPackArea = int(math.ceil(math.sqrt(totalPackArea)) *passedAreaAdditive)

	print '======================================================='
	print "total area"
	print totalPackArea
	print '======================================================='

	print '======================================================='
	print 'bin packer test'

	binPackerObj = binPacker.binPacker(totalPackArea, totalPackArea)
	binPackerObj.fit(passedSortedBlockList)

	for x in range(len(passedSortedBlockList)):
		#print 'Story: ' + passedSortedBlockList[x].story
		print 'Word: ' + passedSortedBlockList[x].word
		print 'Number of Times: ' + str(passedSortedBlockList[x].width)
		print 'X Location: ' + str(passedSortedBlockList[x].fit.x )
		print 'Y Location: ' + str(passedSortedBlockList[x].fit.y)


	print '======================================================='

	return totalPackArea


#return dictionary
#open file
#theShadowOverInnsmouth.txt, AtTheMountainsofMadness.txt, callOfCthulhu.txt     


#constants
#
constAddToSize = 20
constMaxNumberOfWords = 20
constShowAllWords = False
constAreaAdditive = 1.7
totalArea = 0
sortedBlockList =[]
wordLister = {}

#sort Items
#
storyList = ["theShadowOverInnsmouth.txt", "AtTheMountainsofMadness.txt", "callOfCthulhu.txt"]
#storyList = ["AtTheMountainsofMadness.txt"]

#loop thru the list
#
for x in range(len(storyList)):
	wordLister.update(wordParser(storyList[x],wordLister))


sortedBlockList = buildSortedBinList(wordLister,0, constMaxNumberOfWords, constShowAllWords, constAddToSize)
totalArea  = buildPackedBin(sortedBlockList, constAreaAdditive)

#list of colors
#
listOfColors = ['#e8d174','#e39e54','#d64d4d','#4d7358','#9ed670']

#draw items
#
master = Tk()
w = Canvas(master, width=totalArea, height=totalArea)
w.pack()         


for x in range(len(sortedBlockList)):    
	colorNum = randint(0,4) 
	w.create_rectangle(sortedBlockList[x].fit.x, sortedBlockList[x].fit.y, (sortedBlockList[x].fit.x+sortedBlockList[x].width), (sortedBlockList[x].fit.y+sortedBlockList[x].height), fill=listOfColors[colorNum], width=1,outline='black')
	
	#create text
	#
	#w.create_text(sortedBlockList[x].fit.x+10, sortedBlockList[x].fit.y+10, anchor=W, text=sortedBlockList[x].story)
	w.create_text(sortedBlockList[x].fit.x+10, sortedBlockList[x].fit.y+25, anchor=W, text=sortedBlockList[x].word)
	w.create_text(sortedBlockList[x].fit.x+10, sortedBlockList[x].fit.y+45, anchor=W, text=str(sortedBlockList[x].height-constAddToSize))
	
	
mainloop()












