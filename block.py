import numpy as np

class Block:
	'represents a grid element'
	
	position = np.array([ 0 , 0 ])
	field = 0.
	
	def __init__ ( self, xPosition , yPosition ):
		self.position = np.array( [int(xPosition), int(yPosition)])
		
