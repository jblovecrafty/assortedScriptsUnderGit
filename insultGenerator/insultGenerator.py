#!/usr/bin/python
import fileinput
import math
import json
import sys, getopt
from random import randint

###################################################################
# insult generator
###################################################################

#defaults
#
nameOfVictim = "Tim"
severityOfInsult = 1
typeOfInsult = 2
fileLocation = "insultList.txt"
showInsult = True

# Read command line args
myopts, args = getopt.getopt(sys.argv[1:],"v:s:t:h")

###############################
# v == victim name
# s == severity of insult
# t == type of insult
###############################
for o, a in myopts:
	if o == '-v':
		nameOfVictim = a
	elif o == '-s':
		severityOfInsult = int(a)
	elif o == '-t':
		typeOfInsult = int(a)
	elif o == '-h':
		print("Usage: %s -v victim name -s severity of insult as int -t type of insult as int" % sys.argv[0])
		showInsult = False


#open file with JSON
#
fileHandle = open(fileLocation, "r")

#read in JSON to data structure
#
jsonDataStructure = json.load(fileHandle)

#close file
#	
fileHandle.close()


#randomly pick insult
#
maxRandToUse = (len(jsonDataStructure["insults"][severityOfInsult]["listOfInsults"][typeOfInsult]["insultList"])-1)
randomInsult = randint(0, maxRandToUse)
insultType = jsonDataStructure["insults"][severityOfInsult]["listOfInsults"][typeOfInsult]["typeOfInsult"]
#display insult
#
if(showInsult):
	print "Insult Type: " + insultType
	print jsonDataStructure["insults"][severityOfInsult]["listOfInsults"][typeOfInsult]["insultList"][randomInsult] % (nameOfVictim)
	
	