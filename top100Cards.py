##################################
#Find Top 100 Cards and Display 
#Name + Price
##################################
#!/usr/bin/env python

import re
import urllib
from decimal import *

#constant for the web page to scrape
#
topCardPage = "http://findmagiccards.com/Top100/Cards.html"

#dictonary of sets and set mappings
#
dictOfSetMappings = {"IS":"Innistrad", "M12":"2012 Basic Set",  "M11":"2011 Basic Set", "MB":"Mirrodin Besieged", "NP":"New Phyrexia", "SO":"Scars of Mirrodin", "ZE":"Zendikar", "WW":"Worldwake", "RE":"Rise of the Eldrazi", "CM":"Commander", "CM":"Commander",} 

#hold the content of the response
#
pageContentList = []
rankList = 0

htmlStringPatternMain = "<[a-zA-Z0-9]*>(.*?)</[a-zA-Z0-9]*>"
htmlCleanUpPattern = "(<a href=\'.*?\'>)"
#htmlTagCleanUpPattern = "<(.|\n)*?>"
htmlNBSCLeanUp = "&nbsp;"

fileSplitConst = "</TR>"
lineSplitConst = "</TD>"

#download list cards page and store it in a cardList
#
try:
    pageContentList = urllib.urlopen(topCardPage).read().split(fileSplitConst)	

except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)

#snip off first and last bits....cheesy I know but this is a stop gap until I refine the regex
#
pageContentList = pageContentList[1:-1]

for line in pageContentList:
	line = re.sub(htmlCleanUpPattern, "", line)
	line = line.replace(htmlNBSCLeanUp,"")
	line = re.findall(htmlStringPatternMain,line)
	line[1] = dictOfSetMappings[line[1]]
	rankList =(rankList + 1)
	
	print "Name:", line[0], " Set:", line[1], " Ranking:", rankList

