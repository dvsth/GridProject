import numpy as np
import matplotlib.pyplot as plt
import particle as particle
import block as block
import grid as grid

deltaT = 1
gridsize = 25
xAxis = list()
yAxis = list()

p1 = particle.Particle(1 , 2 , 0 , 0)
p2 = particle.Particle(1 , 1 , 0 , 0)

particles = [ p1 , p2]
gridObject = grid.Grid( gridsize )
		
def refresh_blocks () :
	for b in gridObject.blocks:
		b.field = [ 0 , 0 ]
		for p in particles:
			if(p.position.all() != b.position.all()):
				b.field += (p.charge / np.linalg.norm( b.position - p.position )**3 ) * ( b.position - p.position )
		

def refresh_particles () :
	for p in particles:
		f = gridObject.getBlock(p.position).field
		p.velocity = finiteDifferenceV(p.mass , p.charge , f , p.velocity)
		p.position = finiteDifferenceP(p.position , p.velocity)
		xAxis.append(p.position[0])
		yAxis.append(p.position[1])
				
def finiteDifferenceV ( mass , charge , ifield , velocity ) :
	velocity[0] += (charge/mass)* ifield[0] * deltaT
	velocity[1] += (charge/mass)* ifield[1] * deltaT
	
	return velocity
	
def finiteDifferenceP ( position, velocity ) : 
	position[0] += velocity[0] * deltaT
	position[1] += velocity[1] * deltaT
	
	return position
	
	
for time in range(20):
	refresh_blocks()
	refresh_particles()
		

axes = plt.gca()
axes.set_xlim([0 , gridsize])
axes.set_ylim([0 , gridsize])
plt.plot(xAxis , yAxis , 'bo')
plt.show()

