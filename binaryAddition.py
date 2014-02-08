#!/usr/bin/env python
# bit addition

int_1 = 1
int_2 = 1

def binAddition(passedBin1, passedBin2):
	

	andingOp = 1
	xorOp = 0
	
	while(andingOp != 0):
		
		andingOp = passedBin1 & passedBin2
		xorOp = passedBin1 ^ passedBin2
		
		print andingOp
		print xorOp
		
		passedBin1 = andingOp << 1
		passedBin2 = xorOp
		
	return passedBin2
		
		

print binAddition(int_1, int_2)