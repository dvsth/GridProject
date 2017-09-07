import numpy as np
import block as block


class Grid:
	size = 0
	blocks = []
	
	def __init__ (self, size) :
		self.size = size
	
		self.blocks = [ block.Block(x , y) for x in range(size) for y in range(size) ]

		#index = 0
		#for x in range(size):
		#	for y in range(size):
		#		blocks[index] = block.Block(x , y)
		#		index = index + 1
	
	def getBlock ( self, positionVector ) :
		
		x = int(positionVector.item(0))
		y = int(positionVector.item(1))
		if(((x*self.size) + y) < len(self.blocks) - 100 ):
			return self.blocks[(x*self.size) + y]
	
		return self.blocks[0]
