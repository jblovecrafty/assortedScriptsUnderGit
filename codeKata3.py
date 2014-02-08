##################################
#Set up for code kata 3
##################################
#!/usr/bin/env python

import re
from decimal import *
import operator

#This is for the weather.dat page (part a)
####################################################

#function to open the file and return array of all its lines
#
def openFile(passedFileNameToOpen, passedTextToImportStart, passedTextToImportEnd):
	
	#hold the contents of the file we are reading
	#
	listOfFileLines = []
	
	#boolean value to see if we have made it to the preprocessing block
	#
	isPreProcessing = False
	
	try:
		FILE = open(passedFileNameToOpen, 'r')
	
		for lineOfFileBeingRead in FILE:
			
			#do some clean up for the string
			# 
			lineOfFileBeingRead = lineOfFileBeingRead.rstrip()
			lineOfFileBeingRead = lineOfFileBeingRead.lstrip()
			
			lineOfFileBeingRead = re.sub("[\_\-\*\+\=\:\;]*", "", lineOfFileBeingRead)
			
			
			#drop empty lines
			#
			if(lineOfFileBeingRead):
			
				#turn off readling lines into the list
				#	
				if((lineOfFileBeingRead == passedTextToImportEnd)):
					isPreProcessing = False	
			
					#readlines into the list if preProcessing is true
					#
				if(isPreProcessing):
					listOfFileLines.append(lineOfFileBeingRead)
					#print lineOfFileBeingRead
			
				#turn on reading lines into the list
				#	
				if((lineOfFileBeingRead == passedTextToImportStart)):
						isPreProcessing = True
						
	except:
		print "Unexpected error:", sys.exc_info()[0]
	
	return listOfFileLines
	 	

#function to break up the lines of the file and extract the columns we want
#This function creates a list of list (each one being the column) elements and returns them
def columnExtractor(passedList, passedDelimiter):
	
	#returned list
	#
	listOfColumnLists = []
	
	#tempList to hold split up columns
	#
	tempListOfColumns = []
	
	#fire up the split search
	#
	regexSplitter = re.compile(passedDelimiter)
	
	#take passed list and split up the entry and then push it into the list
	#
	for lineInList in passedList:
		
		#split that list
		#
		tempListOfColumns = regexSplitter.split(lineInList)
		listOfColumnLists.append(tempListOfColumns)
		
	#return the list of lists
	return listOfColumnLists

#function to look at the columns and perform the arithmetic that we need
#Take column numbers and subtract them together then put results into list and sort the list and then return it
def columnCalculations(passedList, passedColumnOneLocation, passedColumnTwoLocation, isAdd):
	
	arthitResult = 0
	colOne = 0
	colTwo = 0
	listOfResults = []
	
	#loop thru list
	for listLine in passedList:
				
		colOne = listLine[passedColumnOneLocation]
		colTwo = listLine[passedColumnTwoLocation]
		
		#clean them strings
		#
		colOne = re.sub("(\D+)$", "", colOne)
		colTwo = re.sub("(\D+)$", "", colTwo)

		#convert them to floats
		#
		colOne = float(colOne)
		colTwo = float(colTwo)
						
		#check if we are doing addition or subtraction
		#
		if(isAdd):
			arthitResult = (colOne + colTwo)
		else:
			arthitResult = (colOne - colTwo)
		
		listOfResults.append(arthitResult)
		
		
	return listOfResults

#this function takes a list and set of columns and returns result of them
#
def createColAndResult(passedList, passedLabelCol, passedMathColOne, passedMathColTwo, isAdd):
	
	mathList = []
	finalList = []
	tempList = []
	
	#send of cols to be calculated and put them into a list
	#
	mathList = columnCalculations(list, passedMathColOne, passedMathColTwo, isAdd);
	
	#loop thru list and build dict
	#
	for x in range(0,len(passedList)):
		
		#print passedList[x][passedLabelCol]
		tempList = (passedList[x][passedLabelCol],mathList[x])
		finalList.append(tempList)
	
	return 	finalList
#this is a function that takes a list and sorts it ascending or descending
#
def sortListOfNumbers(passedList, sortColNum):	
	
	#check if sort ascending or desceding sorts
	#
	passedList.sort(key=operator.itemgetter(sortColNum))
	
	return passedList
	

#function that returns the lowest differental between teh max and min
def returnMinMax(passedList):
	
	return passedList[0]
	
				

#function to display  the results
list = columnExtractor(openFile("weather.dat", "Dy MxT   MnT   AvT   HDDay  AvDP 1HrP TPcpn WxType PDir AvSp Dir MxS SkyC MxR MnR AvSLP", "</pre>"), "\s*")

list = createColAndResult(list, 0, 1, 2, False);
#list = openFile("weather.dat", "MMU June 2002", "</pre>")
list = returnMinMax(sortListOfNumbers(list, 1))
print list


