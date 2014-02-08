#!/usr/bin/env python

listToBeSorted = [10,2,4,9,11,12,5,4,7,8,1,2,3]	

#list swapping helping function
#
def swappingHelper(passedList, itemToBeReplacedFirst, itemToBeReplacedLast):
	tempSwap = 0
	
	tempSwap = passedList[itemToBeReplacedFirst]
	passedList[itemToBeReplacedFirst] = passedList[itemToBeReplacedLast]	
	passedList[itemToBeReplacedLast] = tempSwap
	
	return passedList

#selection sort n squared is the time
#
def selectionSort(passedList, passedListTerminus,isAscendingSort):
	
	tempSwap = 0
	numBound = 0
	
	#if isAscendingSort then find lowest number then sort it lowest to highest else highest to lowest
	#
	for counter in range(passedListTerminus, 0, -1):
		
		numBound = counter

		#now loop thru the slice that we are given
		#
		for i in range(0, counter):			
			#asscending or descending test
			#
			if(isAscendingSort):
				if(passedList[i] > passedList[numBound]):		
					numBound = i
					#print "New Max Num is ", passedList[numBound]
			else:
				if(passedList[i] < passedList[numBound]):	
					numBound = i
					#print "New Min Num is ", passedList[numBound]
					
		
		#ok  now lets swap the items in max and passedListTerminus and keep rolling thru
		#
		if(numBound != counter):			
			swappingHelper(passedList, counter, numBound)

	
	print "FINAL ", passedList

#print listToBeSorted
#selectionSort(listToBeSorted, (len(listToBeSorted)-1), True)
#selectionSort(listToBeSorted, (len(listToBeSorted)-1), False)


#Heap and Heap Sort
#

#sift up takes a list, index value, and end of search value
#
def heapSiftUp(passedList, passedIndexValue, passedEndOfSearchValue):
	
	#set left node to 2*i+1
	#
	leftNode = (2*passedIndexValue)+1
	
	#set right to 2*i + 2
	#
	rightNode = (2*passedIndexValue)+2
	
	maxValue = passedIndexValue
	
	#check left and if left array val is bigger than i value then change max value do the same for right also make sure that the left and right values
	#
	if((leftNode <= passedEndOfSearchValue) and (passedList[leftNode] > passedList[maxValue])):
		maxValue = leftNode
		
	if((rightNode <= passedEndOfSearchValue) and (passedList[rightNode] > passedList[maxValue])):
		maxValue = rightNode
	
	#are smaller or equal to the end value otherwise we have an issue
	#if the i and maxvalue dont match then swap and recursively call this same function since we need to sift down the new node sets
	#
	if(maxValue != passedIndexValue):	
		#print "Here at max value ", maxValue, " != ", passedIndexValue 	
		passedList[passedIndexValue], passedList[maxValue] = passedList[maxValue], passedList[passedIndexValue]
		heapSiftUp(passedList, maxValue, passedEndOfSearchValue)
		

# heapify this list
#
def heapify(passedList):
		
	listLength = len(passedList)-1
	index = listLength/2

	for i in range(index,-1,-1):
		heapSiftUp(passedList, i, listLength)
	
	return passedList
	

def heapSort(passedList):
	
	listLength = (len(passedList))-1
	passedList = heapify(passedList)
	
	#now loop thru list and call siftdown on the ever shrinking list
	#
	for i in range(listLength,0, -1):
		passedList[0], passedList[i] = passedList[i], passedList[0]
		listLength = listLength-1
		heapSiftUp(passedList, 0, listLength)
		#print "ITERATION", i, "PASSEDLIST", passedList, "List Length", listLength
		
	
	return passedList
		
		

def printHeap(passedList):
	
	listLength = len(passedList)-1
	index = listLength/2
	
	for i in range(index):
		
		print "Head Node: ", passedList[i]
		
		print "Left Node: ", passedList[(2*i)+1], "    Right Node: ", passedList[(2*i)+2]
		
		print "-------------------------------------------------------------------------"
		
		
def insertionSort(passedList):
	
	listLength = len(passedList)
	
	for outerLoop in range(1, listLength):
		
		index = passedList[outerLoop]
		
		innerLoop = outerLoop
		
		while((innerLoop > 0) and (passedList[innerLoop-1] > index)):
				passedList[innerLoop] = passedList[innerLoop-1]
				innerLoop = innerLoop-1
				
		passedList[innerLoop] = index
		
	return passedList

#shell sort
#
def shellSort(passedList):
	
	#get skip value so we can do the shell sort
	#
	listLength = len(passedList)
	skipValue = listLength//2

	
	#loop over the gaps
	#
	while skipValue > 0:
		#do the insertion sort action
		#
		print "Array Start ", passedList
		for i in range(skipValue, listLength):
			val = passedList[i]
			
			print " PassedList ",passedList , " val ", val, " i ", i	
			
			j = i
			while j >= skipValue and passedList[j-skipValue] > val:
				print " PassedList ",passedList , " val ", val, "Value to look at", passedList[j-skipValue], " j ", j, " i ", i, " step ", (j-skipValue)
				passedList[j] = passedList[j-skipValue]
				
				j -= skipValue
				print " J value ", j
				
			passedList[j] = val
			
		print "Array End   ", passedList
		print "Skip Value  ", skipValue	
		skipValue //=2
	
	return passedList
	
def bubbleSort(passedList):
	
	stillSorting 	= True
	listLength 		= len(passedList)
	tempValue 		= 0
	
	while(stillSorting):
		
		stillSorting = False
		
		for i in range((listLength-1)):
			
			if(passedList[i] > passedList[i+1]):			
				tempValue 		= passedList[i] 
				passedList[i] 	= passedList[i+1]
				passedList[i+1] = tempValue
				stillSorting 	= True
				
	
	return passedList

print "INIT LIST: ",listToBeSorted

#shellSort(listToBeSorted)
#insertionSort(listToBeSorted)
#heapSort(listToBeSorted)
#printHeap(listToBeSorted)
bubbleSort(listToBeSorted)

print "Sorted List: ",listToBeSorted

	