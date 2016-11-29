import math
import numpy as np
import matplotlib.pyplot as plt


class Branch():
	
	def __init__(self, minimum_branch, rotation, sibling_increment, name, parent = None):

		if parent:
			self.start = parent.end
			self.fontsize = 5/6 * parent.fontsize
		else:
			self.fontsize = 15
			self.start = (0, 0)

		end_placement_vector = rotate_vector(minimum_branch.placement_vector, rotation)
		self.end = end_placement_vector.flat[0] + self.start[0], end_placement_vector.flat[1] + self.start[1]
		
		ax.plot([self.start[0], self.end[0]], [self.start[1], self.end[1]], color = 'r')
		ax.text(self.end[0], self.end[1] - 0.5, name, fontsize = self.fontsize, color = 'white', 
			bbox={'facecolor':'blue', 'alpha':0.8, 'pad':2})

		# everything below used exclusively for next generation
		self.branch_vector = np.matrix( [[self.end[0] - self.start[0]], [self.end[1] - self.start[1]]] )
		self.sibling_increment = sibling_increment



class Minimum_Branch():

	def __init__(self, parent = None):

		if parent:
			self.angle_to_parent = (math.pi * 2 - parent.sibling_increment) / 2
			unrotated_placement_vector = (3/4) * parent.branch_vector
			isoceles_angle = (math.pi - self.angle_to_parent) / 2
			self.placement_vector = rotate_vector(unrotated_placement_vector, -isoceles_angle)

		else:
			self.placement_vector = np.matrix( [[2 * BRANCH_LENGTH], [0]] )




def rotate_vector(vector, rotation_theta):
	rotation_matrix = np.matrix([ [math.cos(rotation_theta), -math.sin(rotation_theta)], [math.sin(rotation_theta), math.cos(rotation_theta)] ])
	return np.dot(rotation_matrix, vector)




def create_nuclear_family(possiblities, parent = None):

	minimum_branch = Minimum_Branch(parent)

	if parent:
		range = math.pi * 2 - minimum_branch.angle_to_parent * 2 + math.pi / 30 # going a little past parallel
		sibling_increment = range / (len(possiblities) - 1)
	else:
		sibling_increment = math.pi * 2 / len(possiblities)


	family = []
	for i, p in enumerate(possiblities):
		family.append(Branch(minimum_branch = minimum_branch, rotation = sibling_increment * i, 
			sibling_increment = sibling_increment, parent = parent, name = p))

	return family




fig = plt.figure()
ax = fig.add_subplot(111)

BRANCH_LENGTH = 4
top_level_branches = create_nuclear_family(['A', 'B', 'C',1,1,1])
for tlb in top_level_branches:
	a = create_nuclear_family(['A', 'B', 'C',1,1,1], tlb)
	for aa in a:
		b = create_nuclear_family([1,2,3], aa)



plt.show()


