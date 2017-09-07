import numpy as np

class Particle:
	'represents a particle'
	
	position = np.array([ 0 , 0 ])
	velocity = np.array([ 0 , 0 ])
	charge = 1.
	mass = 1.
	
	def __init__ ( self, xPosition , yPosition , xVelocity , yVelocity ):
		self.position = np.array([int(xPosition), int(yPosition)])
		self.velocity = np.array([int(xVelocity), int(yVelocity)])
		
	def getCurrentPosition () :
		return position 
		
	def getCurrentVelocity () : 
		return velocity
