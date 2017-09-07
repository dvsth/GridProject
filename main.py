import numpy as np
import matplotlib.pyplot as plt
import particle as particle
import block as block
import grid as grid

deltaT = 1
gridsize = 100

p1xAxis = list()
p1yAxis = list()

p2xAxis = list()
p2yAxis = list()

p3xAxis = list()
p3yAxis = list()

p1 = particle.Particle(20 , 20 , 1 , 2)
p2 = particle.Particle(23 , 24 , 3 , 1)
p3 = particle.Particle(30 , 25 , 3 , 0)

particles = [ p1 , p2 , p3 ]
gridObject = grid.Grid( gridsize )
		
def refresh_blocks () :
	for b in gridObject.blocks:
		b.field = [ 0 , 0 ]
		for p in particles:
			if((p.position[0] != b.position[0]) and (p.position[1] != b.position[1])):
				b.field += (p.charge / np.linalg.norm( b.position - p.position )**3 ) * ( b.position - p.position )
				#print 'difference of positions : ' + str( b.position - p.position )
				#print 'norm of difference:       ' + str( np.linalg.norm( b.position - p.position ) )
		print (str(b.position) + str(b.field))		

def refresh_particles () :
	#for p in particles:
	#	xPos = list()
	#	yPos = list()
	#	f = gridObject.getBlock(p.position).field
	#	print ('field = ' + str(f))
	#	p.velocity = finiteDifferenceV(p.mass , p.charge , f , p.velocity)
	#	p.position = finiteDifferenceP(p.position , p.velocity)
	#	xPos.append(p.position[0])
	#	yPos.append(p.position[1])
		
	#	print p.position
	
	f1 = gridObject.getBlock(p1.position).field
	p1.velocity = finiteDifferenceV(p1.mass , p1.charge , f1 , p1.velocity)
	p1.position = finiteDifferenceP(p1.position , p1.velocity)
	p1xAxis.append(p1.position[0])
	p1yAxis.append(p1.position[1])
	print 'position' + str(p1.velocity) 
	print 'velocity' + str(p1.position)
	f2 = gridObject.getBlock(p2.position).field
	p2.velocity = finiteDifferenceV(p2.mass , p2.charge , f2 , p2.velocity)
	p2.position = finiteDifferenceP(p2.position , p2.velocity)
	p2xAxis.append(p2.position[0])
	p2yAxis.append(p2.position[1])
	f3 = gridObject.getBlock(p3.position).field
	p3.velocity = finiteDifferenceV(p3.mass , p3.charge , f3 , p3.velocity)
	p3.position = finiteDifferenceP(p3.position , p3.velocity)
	p3xAxis.append(p3.position[0])
	p3yAxis.append(p3.position[1])

def finiteDifferenceV ( mass , charge , ifield , velocity ) :
	velocity[0] += (charge/mass)* ifield[0] * deltaT
	velocity[1] += (charge/mass)* ifield[1] * deltaT
	print 'velocity' + str(velocity)
	return velocity
	
def finiteDifferenceP ( position, velocity ) : 
	position[0] += velocity[0] * deltaT
	position[1] += velocity[1] * deltaT
	
	return position
	
count = 0
for time in range(20):
	refresh_blocks()
	refresh_particles()
	count = count + 1
	print count

axes = plt.gca()
axes.set_xlim([0 , gridsize])
axes.set_ylim([0 , gridsize])
plt.plot(p1xAxis , p1yAxis , 'bo')
plt.plot(p2xAxis , p2yAxis , 'ro')
plt.plot(p3xAxis , p3yAxis , 'ko')
plt.show()

