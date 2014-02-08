##################################
#Set up
##################################
#!/usr/bin/env python
import threading
import time

# master test list for the rest of methods
#
exampleList = [1,2,3,4,5,6,7,8,9,10,11]

mainExampleListTrueLength = (len(exampleList)-1)

##################################


##################################
#function to binary chop iterativly
##################################
def binaryChopIt(passedList, passedNumberToSearchFor):
	#take passed number to search for and look for it in the array
	#
	minNum = 0
	maxNum = (len(passedList)-1)
	midNum = 0
	
	#the function to put it all together
	#
	while( minNum <= maxNum ):
		
		midNum = (minNum + maxNum)/2
		print "minNum " , minNum , " maxNum " , maxNum , " midNum " , midNum
		
		if(passedList[midNum] == passedNumberToSearchFor):
			return passedList[midNum]
		
		elif(passedList[midNum] < passedNumberToSearchFor):
			minNum = midNum+1
			
		elif(passedList[midNum] > passedNumberToSearchFor):
			maxNum = midNum - 1

		
##################################	
#binary recursive function
##################################
def binaryChopRec(passedList, passedMinNum, passedMaxNum, passedNumberToSearchFor):
	
	midNum = (passedMaxNum + passedMinNum)/2
	
	print "minNum " , passedMinNum , " maxNum " , passedMaxNum , " midNum " , midNum
	
	#First lets make sure that we havent lapped ourselves looking for a non existent number
	#
	if(passedMinNum > passedMaxNum):
		return
		
	elif(passedList[midNum] == passedNumberToSearchFor):
		return passedList[midNum]
	
	elif(passedList[midNum] < passedNumberToSearchFor):
		passedMinNum = midNum+1
		return binaryChopRec(passedList, passedMinNum, passedMaxNum, passedNumberToSearchFor)
		
		
	elif(passedList[midNum] > passedNumberToSearchFor):
		passedMaxNum = midNum - 1
		return binaryChopRec(passedList, passedMinNum, passedMaxNum, passedNumberToSearchFor)
		


##################################
#Stage one of binary chop that is the master/contoller
#stage one passes lists to stage two and stage two slices the list down into smaller and smaller lists until
#the second stage returns a list of one
##################################
def binaryChopStageOne(passedList, passedNum):
	
	while(len(passedList) > 1):
		#call and set passedList to passedList
		#
		passedList = binaryChopStageTwo(passedList, passedNum)
		
	return passedList;


##################################
#Stage two of the binary chop that is the worker
##################################
def binaryChopStageTwo(passedList, passedNumberToSearchFor):
	
	minNum = 0
	maxNum = (len(passedList)-1)
	midNum = 0
	
	midNum = (minNum + maxNum)/2
	
	print "minNum " , minNum , " maxNum " , maxNum , " midNum " , midNum, " Length of List ", len(passedList)
	
	if(passedList[midNum] == passedNumberToSearchFor):
		return passedList[midNum:midNum]
	
	elif(passedList[midNum] < passedNumberToSearchFor):
		minNum = midNum+1
		return passedList[minNum:maxNum]
		
	elif(passedList[midNum] > passedNumberToSearchFor):
		maxNum = midNum - 1
		return passedList[minNum:maxNum]
		


##################################
#recursive version of stage one
##################################
def binaryChopStageOneRec(passedList, passedMinNum, passedMaxNum, passedNumberToSearchFor):
	
	print "starting recursion"	
	
	#call and set passedList to passedList
	#
	passedList = binaryChopStageTwoRec(passedList, passedMinNum, passedMaxNum, passedNumberToSearchFor)
	
	print "done with recursion"	
	return passedList;	

	
##################################
#binary recursive function second stage
##################################
def binaryChopStageTwoRec(passedList, passedMinNum, passedMaxNum, passedNumberToSearchFor):

	midNum = (passedMaxNum + passedMinNum)/2
	print "minNum " , passedMinNum , " maxNum " , passedMaxNum , " midNum " , midNum

	#First lets make sure that we havent lapped ourselves looking for a non existent number
	#
	if(passedMinNum > passedMaxNum):

		return
		
	elif(passedList[midNum] == passedNumberToSearchFor):
		return passedList[midNum]

	elif(passedList[midNum] < passedNumberToSearchFor):
		passedMinNum = midNum+1
		return binaryChopStageTwoRec(passedList, passedMinNum, passedMaxNum, passedNumberToSearchFor)


	elif(passedList[midNum] > passedNumberToSearchFor):
		passedMaxNum = midNum - 1
		return binaryChopStageTwoRec(passedList, passedMinNum, passedMaxNum, passedNumberToSearchFor)


##################################
#Thread based binary chop
##################################
def binaryChopThread(passedList, passedNumberToSearchFor):
	
	#split the array into two pieces and then let the threads do the 
	#work 
	#TODO use the threads in a meaningful way
	# 
	
	#split up the array into two chunks
	#
	midNum = (len(passedList))/2
	
	firstList 	=  passedList[:midNum]
	secondList 	=  passedList[midNum:]	
	
	firstThread 	= threading.Thread(name='firstThread', target=binaryChopThreadWorker, args=(firstList,passedNumberToSearchFor))
	secondThread 	= threading.Thread(name='secondThread', target=binaryChopThreadWorker, args=(secondList,passedNumberToSearchFor))

	#start them up
	#
	firstThread.start()
	secondThread.start()

##################################
#Thread based binary chop worker
##################################	
def binaryChopThreadWorker(passedList, passedNumberToSearchFor):

	#take passed number to search for and look for it in the array
	#
	minNum = 0
	maxNum = (len(passedList)-1)
	midNum = 0
	
	#the function to put it all together
	#
	while( minNum <= maxNum ):
	
		midNum = (minNum + maxNum)/2
		
		if(passedList[midNum] == passedNumberToSearchFor):
			print passedList[midNum]
			return passedList[midNum]
			
		elif(passedList[midNum] < passedNumberToSearchFor):
			minNum = midNum +1
			
		elif(passedList[midNum] > passedNumberToSearchFor):
			maxNum = midNum - 1


##################################
#Valid Number to Seach for Test(s)
##################################
#print "Valid Number to Seach for Test(s)"
#print binaryChopIt(exampleList, 7)
#print len(exampleList)
#print binaryChopRec(exampleList, 0, mainExampleListTrueLength, 7)
#print binaryChopStageOne(exampleList, 7)
#print binaryChopStageOneRec(exampleList, 0, mainExampleListTrueLength, 7)
#print binaryChopThread(exampleList, 7)

##################################
#Invalid Number to Seach for Test(s)
##################################
#print "Invalid Number to Seach for Test(s)"
#print binaryChopIt(exampleList, 17)
#print len(exampleList)
#print binaryChopRec(exampleList, 0, mainExampleListTrueLength, 17)
#print binaryChopStageOne(exampleList, 17)
#print binaryChopStageOneRec(exampleList, 0, mainExampleListTrueLength, 17)
#print binaryChopThread(exampleList, 17)