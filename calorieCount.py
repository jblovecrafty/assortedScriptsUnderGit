#!/usr/bin/env python
import os.path

#vars and constants
#
QUITVALUE = "Q"
CALORIEFILERECORDER = "calFile.txt"
currentInput = ""
currentTotalsCalories = 0

#perform init actions
#
if(os.path.exists(CALORIEFILERECORDER)):
	
	fileHandler = open(CALORIEFILERECORDER,'r+')
	currentTotalsCalories = fileHandler.read()	
	currentTotalsCalories = currentTotalsCalories.strip()

	#Check if string is empty
	#
	if currentTotalsCalories:
		print "Previous Calories ", currentTotalsCalories
	else:
		print "Zero"
		currentTotalsCalories = 0
		
	fileHandler.close()

#collect input
#
while(currentInput != QUITVALUE):
	currentInput = raw_input("Enter the Calories: ")
	
	if(currentInput != QUITVALUE):
		currentTotalsCalories = int(currentTotalsCalories) + int(currentInput)
		print currentTotalsCalories

writeFileHandler = open(CALORIEFILERECORDER,'w')
writeFileHandler.write(str(currentTotalsCalories))
writeFileHandler.close()
	
print "Your Calories Are: ", currentTotalsCalories
	
	

