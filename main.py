import numpy as np
import matplotlib.pyplot as plt
import particle as particle
import block as block
import grid as grid


p1 = particle.Particle(2 , 2)
p2 = particle.Particle(0 , 0)

particles = [ p1 , p2 ]

for time in range(2):
		
def refresh_blocks () :
	for b in grid.blocks:
		b.field = 0
		for p in particles:
			if(p.position != b.position):
				b.field += (p.charge / np.linalg.norm( b.position - p.position )**3 ) * ( b.position - p.position )
		print (b.field)

def refresh_particles () :
	for p in particles:
		p.velocity += finiteDifference(p.mass , p.charge , )
		
			

