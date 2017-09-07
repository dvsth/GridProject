import numpy as np
import block as block

size = 0

def __init__ (self, size) :
	self.size = size
	
	blocks = [ block.Block(x , y) for x in range(size) for y in range(size) ]

	#index = 0
	#for x in range(size):
	#	for y in range(size):
	#		blocks[index] = block.Block(x , y)
	#		index = index + 1
	
def getBlock ( positionVector )
	x = int(positionVector.item(0))
	y = int(positionVector.item(1))
	return blocks[(x*size) + y]
