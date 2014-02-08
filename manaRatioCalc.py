from __future__ import division
#!/usr/bin/env python
import math

#TEST DATA
#
testList = {'Blue' : 10,'Red' : 9,'Green' : 9}
testNumberOfLandCards = 17

#Vars and Constants
#
MAXNUMBEROFCOLORS = 5
totalCards = 0
landBreakDown = {}
colorAndNumberDict = {}
numberOfLands = 0

#instructions for the user
#
INITIALPROMPT = "Please enter the number of colors you are using "
COLORPROMPT = "Please Enter The Name of the Color "
CARDNUMBERPROMPTFORCOLOR = "Please Enter the Number of Cards in this Color "
LANDCARDNUMBERPROMPT = "Please Enter the Number of Lands for this Deck "

#Function for user interface TODO: Clean up and remove references to global vars
#
def userInterFaceForColors(passedDict):
	#prompt User
	#
	numberOfColors = int(raw_input(INITIALPROMPT))

	#keep them in a loop until we get the nunmber
	#
	while((numberOfColors > MAXNUMBEROFCOLORS) or (numberOfColors <= 0)):
		numberOfColors = int(raw_input(INITIALPROMPT))

	for i in range(numberOfColors, 0, -1):
	
		#gather the name of color cards
		#TODO error check the color names
		#
		tempColor = raw_input(COLORPROMPT)

		#ask for number of colors
		#
		tempNumber = int(raw_input(CARDNUMBERPROMPTFORCOLOR))
	
		#now add the name value pair to list
		#
		passedDict[tempColor] = tempNumber
		
	return passedDict
	

def userInterFaceForLands(passedNumberOfLands):
	#get number of lands wanted
	#
	numbOfLands = int(raw_input(LANDCARDNUMBERPROMPT))
	
	return numbOfLands


def calculateTotalCards(passedDict):
	
	cardsTotal = 0
	
	#add up the total number of cards
	#
	for key in passedDict.iterkeys():
		cardsTotal += passedDict[key]

	return cardsTotal
	

#method to calculate the mana ratio
#
def calculateManaRatio(passedDictOfCards, passedTotalCards, passedTotalLandCards):
	
	manaRatioList = []
	tempList = []
	
	#ok loop thru the list and calculate the mana
	#
	for key in passedDictOfCards.iterkeys():
		
		tempList.append(key)
		
		manaRatio = round(int(passedDictOfCards[key])/int(passedTotalCards),2)
		tempList.append(manaRatio)
		print manaRatio
		
		#ok if the percentage is over fifty percent then ceil else floor
		#
		if(manaRatio > round(1/len(passedDictOfCards),2)):	
			manaTotal = math.floor(manaRatio * passedTotalLandCards)
		else:
			manaTotal = math.ceil(manaRatio * passedTotalLandCards)
		
		tempList.append(manaTotal)
		
		# add to the list
		#
		manaRatioList.append(tempList)
		
		#clear temp list
		#
		tempList = []
	
	#ok if the total cards dont add up to the input of land then we have an issue
	#
	return manaRatioList
	

#MAIN METHOD HERE
colorAndNumberDict 	= userInterFaceForColors(colorAndNumberDict)
numberOfLands 		= userInterFaceForLands(numberOfLands)
totalCards 			= calculateTotalCards(colorAndNumberDict)

lister = calculateManaRatio(colorAndNumberDict, totalCards, numberOfLands)	
print lister
	

