#!/usr/bin/python
from decimal import *

###################################
## Markov Chain Experiment
###################################
#decimal precision
#
getcontext().prec = 3

#probabilities for sunny or rainy
#
sunnyToSunny = .8
sunnyToRainy = .2

rainyToSunny = .5
rainyToRainy = .5

numberOfTimesToRunMatrixMult = 200

#matrixes
#
probMatrix = [[sunnyToSunny,sunnyToRainy],[rainyToSunny ,rainyToRainy]]

#start with and indentity matrix
#
resultMatrix = [[1,0], [0,1]]

#keep this guy at 0 since we are adding to him
#
tempResultMatrix = [[0,0], [0,0]]

#do the work
#
for x in range (numberOfTimesToRunMatrixMult):

	# iterate through rows of probMatrix
	#
	for i in range(len(probMatrix)):

		# iterate through columns of resultMatrix
		#
		for j in range(len(resultMatrix[0])):

			#iterate through the rows of resultMatrix
			#
			for k in range(len(resultMatrix)):
				#print probMatrix[i][k]
				#print resultMatrix[k][j]
				#print resultMatrix[i][j]
				#print '============================='
				tempResultMatrix[i][j] += Decimal(probMatrix[i][k]) * Decimal(resultMatrix[k][j])

	#now set the result matrix to the tempresult matrix
	#
	resultMatrix = tempResultMatrix

	#reset temp
	#
	tempResultMatrix = [[0,0], [0,0]]

for r in resultMatrix:
   print(r)
