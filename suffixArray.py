#!/usr/bin/env python

#turn string into array
#
string = 'abaaacazxa'
stringList = list(string)

#ok now loop thru a progressly bigger string to build suffix array
#
suffixList = []
startPoint = 0

for i in (stringList):
	suffixList.append(''.join(stringList[startPoint:]))
	startPoint+=1

suffixList.sort()
print suffixList
print len(suffixList)


#ok lets create a LongestCommonPrefix listing for the new storted list
#
LCPList = []

#loop thru stringList take stringList[i] and stringList[i-1]
#
for k in range(len(suffixList)):
	if(k >= 0):
		LCPCount = 0
		ithSuffix = list(suffixList[k])
		ithMinusOneSuffix = list(suffixList[k-1])
		iterationRange = 0

		# find shortest length and use that as range
		#
		if(len(ithSuffix) <= len(ithMinusOneSuffix)):
			iterationRange = len(ithSuffix) 
			#print len(ithSuffix)
		else:
			iterationRange = len(ithMinusOneSuffix) 
			#print len(ithMinusOneSuffix)
		
		
		#inner loop from start of i and compare it to i-1 for similaritty increment by one else break
		#
		for j in range(iterationRange):
			#print str(j) + " jth iteration " + ithSuffix[j] + " == " + ithMinusOneSuffix[j] + " on ith iteration " + suffixList[k]
			if(ithSuffix[j] == ithMinusOneSuffix[j]):
				LCPCount+=1
			else:
				#print "Breaking out at " + str(k)
				break	
		LCPList.append(LCPCount)

print LCPList	
print len(LCPList)			

