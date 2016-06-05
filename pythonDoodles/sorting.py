#!/usr/bin/python
import math

#selection sort
#
def selectionSort(passedList):
	index = 0
	
	#ok first lets loop thru the array
	#
	for index in range(len(passedList)):
		# ok now lets find the largest item in the array 
		# set up the current max that we think along with its index and subCurrentMax
		#
		currentMax = passedList[index]
		indexOfLargest = index
		subCurrentMax = currentMax
		
		#now find the largest in our set
		#	
		for subIndex in range((index+1),len(passedList)):
			tempMax = passedList[subIndex]
			
			# if tempMax > subCurrentMax swap
			# 
			if(tempMax > subCurrentMax):
				# ok we have a contender so lets call it the sub max and move on
				#
				subCurrentMax = passedList[subIndex]
				indexOfLargest = subIndex
		
		# now that the largest item is found lets swap it with the current item in the array and update index var
		#
		tempIndex = currentMax
		passedList[index] = passedList[indexOfLargest]
		passedList[indexOfLargest] = currentMax
		
	return passedList
	
#insertion sort
#
def insertionSort(passedList):
	#start with first item and compare it to its neighbor
	#
	for index in range(1,len(passedList)):
		
		sortedUpperBound = index-1
		maxValue = passedList[index]
		
		#ok now lets hold here until either  passedList[sortedUpperBound] < maxValue
		# and sortedUpperBound >= 0
		#
		while((passedList[sortedUpperBound] < maxValue) and (sortedUpperBound >= 0)):
			
			passedList[sortedUpperBound+1] = passedList[sortedUpperBound]
			
			sortedUpperBound -= 1
		
		
		passedList[sortedUpperBound+1] = maxValue
		
	return passedList
	
#shell sort
#
def shellSort(passedList):
	
	#first get our gaps
	# 
	lengthOfList = len(passedList)
	gap = int(math.floor(lengthOfList/2))
	
	#continue while gap is greater than 0
	#
	while(gap > 0):
	
		#then do an insertion sort based on those gaps
		#
		for index in range(gap,lengthOfList):
			
			#set up the temp value for the index based on gap size
			#
			tempValue = passedList[index]
			
			#set up sub index so we can decrement it as we see fit when placing the item
			#
			subIndex = index
			
			#ok now let us do our loop only keep in loop if the tempvalue is less than the subindex-gap
			#and if the subindex is greater or equal to the gap
			#
			while((passedList[subIndex-gap] < tempValue) and (subIndex >= gap)):
				
				#move item next to the subindex in question to the next gap over
				#
				passedList[subIndex] = passedList[subIndex-gap]
				
				#decrement the gap as we move down the array
				#
				subIndex -= gap
			
			#update the subindex value with the new value it should be
			#
			passedList[subIndex] = tempValue
				
			
		#increment gap
		#
		print '==================='
		print gap
		print passedList
		print '==================='
		gap = int(math.floor(gap/2))
	
	return passedList


#merge sort function
#
def mergeSort(passedArray):
	
	#base case already sorted so just return out
	#
	if(len(passedArray)<= 1):
		return passedArray
		
	#figure out mid point and contents of the left and right arrays
	#
	midPoint 	= len(passedArray)/2
	rightHalf 	= passedArray[midPoint:]
	leftHalf	= passedArray[:midPoint]
	
	print '==================='
	print "left half"
	print leftHalf
	print "right half"
	print rightHalf
	print '==================='	
	print "\n"
		
	#make two recursive calls one for the right and one for the left
	#
	leftHalf 	= mergeSort(leftHalf)
	rightHalf 	= mergeSort(rightHalf)
		
	#merge results and return as list
	#
	return list(mergeResults(leftHalf, rightHalf))
		

#merging function
#
def mergeResults(passedLeftHalfArray, passedRightHalfArray):
	
	# the trick to this is to keep comparing the left and right sides and then building a list from the
	# results of the comparison
	#
	leftHalfStart  = 0
	leftHalfEnd	= len(passedLeftHalfArray)
	
	rightHalfStart	= 0
	rightHalfEnd 	= len(passedRightHalfArray)
	
	#init temp list
	#
	tempList = []
	
	# only keep this going until either beginning indexes exceeds the end
	# we see which item is bigger and add it to the tempList
	#
	while((leftHalfStart < leftHalfEnd) and (rightHalfStart < rightHalfEnd) ):
		
		if(passedLeftHalfArray[leftHalfStart] >= passedRightHalfArray[rightHalfStart]):
			
			tempList.append(passedLeftHalfArray[leftHalfStart])
			leftHalfStart +=1
			
		else:
			
			tempList.append(passedRightHalfArray[rightHalfStart])
			rightHalfStart +=1
	
	#ok now lets check if we have any left overs from either list
	# and add them to the templist
	#
	if passedLeftHalfArray:
		tempList.extend(passedLeftHalfArray[leftHalfStart:])
		
	if passedRightHalfArray:
		tempList.extend(passedRightHalfArray[rightHalfStart:])
	
	return tempList
	
# pivot sort
#
def pivotSort(passedList, passedStartIndex, passedEndIndex):

	#check if start is bigger than end if it is return list
	#
	if(passedStartIndex < passedEndIndex):
		
		#ok now let us do some partitioning
		#
		pivot = pivotPartition(passedList, passedStartIndex, passedEndIndex)
		
		#ok now lets recursively make calls to pivot sort
		#
		pivotSort(passedList, passedStartIndex, pivot-1)
		pivotSort(passedList, pivot+1, passedEndIndex)
		
		
	#now return list
	#
	return passedList
		
# helper function for sorting and finding a pivot for the pivotSort
#
def pivotPartition(passedList, passedStartIndex, passedEndIndex):
	
	#first markout the pivot we are to use
	#
	pivot = passedList[passedStartIndex]
	
	#set up right and left pointers
	#Left pointer is start index+1 so we create a free space for the pivot
	#
	leftPointer 	= passedStartIndex+1
	rightPointer 	= passedEndIndex
	
	done = False
	
	#loop until we are done with comparisons
	#
	while not done:
		
		# search thru the left side and make sure that we only stop
		# if leftPointer is less than rightPointer and leftPointer value
		# is less than pivot
		#
		while((leftPointer <=  rightPointer) and (passedList[leftPointer] <= pivot)):
			leftPointer += 1
			
		# search thru t#!/usr/bin/python
import math

#selection sort
#
def selectionSort(passedList):
	index = 0
	
	#ok first lets loop thru the array
	#
	for index in range(len(passedList)):
		# ok now lets find the largest item in the array 
		# set up the current max that we think along with its index and subCurrentMax
		#
		currentMax = passedList[index]
		indexOfLargest = index
		subCurrentMax = currentMax
		
		#now find the largest in our set
		#	
		for subIndex in range((index+1),len(passedList)):
			tempMax = passedList[subIndex]
			
			# if tempMax > subCurrentMax swap
			# 
			if(tempMax > subCurrentMax):
				# ok we have a contender so lets call it the sub max and move on
				#
				subCurrentMax = passedList[subIndex]
				indexOfLargest = subIndex
		
		# now that the largest item is found lets swap it with the current item in the array and update index var
		#
		tempIndex = currentMax
		passedList[index] = passedList[indexOfLargest]
		passedList[indexOfLargest] = currentMax
		
	return passedList
	
#insertion sort
#
def insertionSort(passedList):
	#start with first item and compare it to its neighbor
	#
	for index in range(1,len(passedList)):
		
		sortedUpperBound = index-1
		maxValue = passedList[index]
		
		#ok now lets hold here until either  passedList[sortedUpperBound] < maxValue
		# and sortedUpperBound >= 0
		#
		while((passedList[sortedUpperBound] < maxValue) and (sortedUpperBound >= 0)):
			
			passedList[sortedUpperBound+1] = passedList[sortedUpperBound]
			
			sortedUpperBound -= 1
		
		
		passedList[sortedUpperBound+1] = maxValue
		
	return passedList
	
#shell sort
#
def shellSort(passedList):
	
	#first get our gaps
	# 
	lengthOfList = len(passedList)
	gap = int(math.floor(lengthOfList/2))
	
	#continue while gap is greater than 0
	#
	while(gap > 0):
	
		#then do an insertion sort based on those gaps
		#
		for index in range(gap,lengthOfList):
			
			#set up the temp value for the index based on gap size
			#
			tempValue = passedList[index]
			
			#set up sub index so we can decrement it as we see fit when placing the item
			#
			subIndex = index
			
			#ok now let us do our loop only keep in loop if the tempvalue is less than the subindex-gap
			#and if the subindex is greater or equal to the gap
			#
			while((passedList[subIndex-gap] < tempValue) and (subIndex >= gap)):
				
				#move item next to the subindex in question to the next gap over
				#
				passedList[subIndex] = passedList[subIndex-gap]
				
				#decrement the gap as we move down the array
				#
				subIndex -= gap
			
			#update the subindex value with the new value it should be
			#
			passedList[subIndex] = tempValue
				
			
		#increment gap
		#
		print '==================='
		print gap
		print passedList
		print '==================='
		gap = int(math.floor(gap/2))
	
	return passedList


#merge sort function
#
def mergeSort(passedArray):
	
	#base case already sorted so just return out
	#
	if(len(passedArray)<= 1):
		return passedArray
		
	#figure out mid point and contents of the left and right arrays
	#
	midPoint 	= len(passedArray)/2
	rightHalf 	= passedArray[midPoint:]
	leftHalf	= passedArray[:midPoint]
	
	print '==================='
	print "left half"
	print leftHalf
	print "right half"
	print rightHalf
	print '==================='	
	print "\n"
		
	#make two recursive calls one for the right and one for the left
	#
	leftHalf 	= mergeSort(leftHalf)
	rightHalf 	= mergeSort(rightHalf)
		
	#merge results and return as list
	#
	return list(mergeResults(leftHalf, rightHalf))
		

#merging function
#
def mergeResults(passedLeftHalfArray, passedRightHalfArray):
	
	# the trick to this is to keep comparing the left and right sides and then building a list from the
	# results of the comparison
	#
	leftHalfStart  = 0
	leftHalfEnd	= len(passedLeftHalfArray)
	
	rightHalfStart	= 0
	rightHalfEnd 	= len(passedRightHalfArray)
	
	#init temp list
	#
	tempList = []
	
	# only keep this going until either beginning indexes exceeds the end
	# we see which item is bigger and add it to the tempList
	#
	while((leftHalfStart < leftHalfEnd) and (rightHalfStart < rightHalfEnd) ):
		
		if(passedLeftHalfArray[leftHalfStart] >= passedRightHalfArray[rightHalfStart]):
			
			tempList.append(passedLeftHalfArray[leftHalfStart])
			leftHalfStart +=1
			
		else:
			
			tempList.append(passedRightHalfArray[rightHalfStart])
			rightHalfStart +=1
	
	#ok now lets check if we have any left overs from either list
	# and add them to the templist
	#
	if passedLeftHalfArray:
		tempList.extend(passedLeftHalfArray[leftHalfStart:])
		
	if passedRightHalfArray:
		tempList.extend(passedRightHalfArray[rightHalfStart:])
	
	return tempList
	
# pivot sort that only requires one array
#
def pivotSort(passedList, passedStartIndex, passedEndIndex):

	#check if start is bigger than end if it is return list
	#
	if(passedStartIndex < passedEndIndex):
		
		#ok now let us do some partitioning
		#
		pivot = pivotPartition(passedList, passedStartIndex, passedEndIndex)
		
		#ok now lets recursively make calls to pivot sort
		#
		pivotSort(passedList, passedStartIndex, pivot-1)
		pivotSort(passedList, pivot+1, passedEndIndex)
		
		
	#now return list
	#
	return passedList
		
# helper function for sorting and finding a pivot for the pivotSort
#
def pivotPartition(passedList, passedStartIndex, passedEndIndex):
	
	#first markout the pivot we are to use
	#
	pivot = passedList[passedStartIndex]
	
	#set up right and left pointers
	#Left pointer is start index+1 so we create a free space for the pivot
	#
	leftPointer 	= passedStartIndex+1
	rightPointer 	= passedEndIndex
	
	done = False
	
	#loop until we are done with comparisons
	#
	while not done:
		
		# search thru the left side and make sure that we only stop
		# if leftPointer is less than rightPointer and leftPointer value
		# is less than pivot
		#
		while((leftPointer <=  rightPointer) and (passedList[leftPointer] <= pivot)):
			leftPointer = leftPointer + 1
			
		# search thru the right side and make sure that we only stop
		# if rightPointer is greater than leftPointer and rightPointer value
		# is greater than pivot
		#
		while((passedList[rightPointer] >= pivot) and (rightPointer >=  leftPointer)):
			rightPointer = rightPointer -1
		
		# check if we have crossed pointers
		#
		if(rightPointer < leftPointer):
			done = True
		else:
			# time to swap elements from the left side to the right side
			# 
			tempValue 					= passedList[leftPointer]
			passedList[leftPointer] 	= passedList[rightPointer]
			passedList[rightPointer] 	= tempValue
	
	# ok now that we are all done sorting the list according to the pivot let us now swap the startIndex
	# with the right pointer
	#
	tempValuePivot 					= passedList[passedStartIndex]
	passedList[passedStartIndex]  	= passedList[rightPointer] 
	passedList[rightPointer]  		= tempValuePivot
	
	return rightPointer
	


arrayToSort = ['2', '1',  '5', '4', '2', '6']
#print shellSort(arrayToSort)
#print mergeSort(arrayToSort)

print pivotSort(arrayToSort, 0, len(arrayToSort)-1)



