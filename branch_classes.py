import math
import numpy as np
import matplotlib.pyplot as plt

from utility_fxns import *

class Branch():
	
	def __init__(self, axes, minimum_branch, rotation, sibling_increment, name, parent = None):

		end_placement_vector = rotate_vector(minimum_branch.placement_vector, rotation)
		self.parent = parent
		self.name = name
		self.axes = axes

		if parent:
			self.start = parent.end
			self.fontsize = 5/6 * parent.fontsize
			self.end = end_placement_vector.flat[0] + parent.start[0], end_placement_vector.flat[1] + parent.start[1]

			if rotation != 0:
				plot_placement_vectors(axes, parent.start, minimum_branch.placement_vector, rotation)

		else:
			self.fontsize = 15
			self.start = (0, 0)
			self.end = end_placement_vector.flat[0] + self.start[0], end_placement_vector.flat[1] + self.start[1]
		

		self.plot_branch()
		# everything below used exclusively for next generation
		self.branch_vector = np.matrix( [[self.end[0] - self.start[0]], [self.end[1] - self.start[1]]] )
		self.sibling_increment = sibling_increment



	def plot_branch(self):
		if self.parent:
			self.fontsize = 5/6 * self.parent.fontsize
		else:
			self.fontsize = 15

		self.axes.plot([self.start[0], self.end[0]], [self.start[1], self.end[1]], color = 'r', linewidth = 2)
		self.axes.plot([self.end[0]],[self.end[1]], 'bo')
		plt.pause(0.1)



	def label_branch(self):
		self.axes.text(self.end[0], self.end[1] - 0.25, self.name, fontsize = self.fontsize, color = 'white', 
			bbox={'facecolor':'blue', 'alpha':0.8, 'pad':4})



class Minimum_Branch():

	def __init__(self, axes, branch_length, parent = None):

		if parent:
			self.angle_to_parent = (math.pi * 2 - parent.sibling_increment) / 2
			self.isoceles_angle = (math.pi - self.angle_to_parent) / 2
			placement_vect_len = math.cos(self.isoceles_angle) * branch_length * 2
			scale_factor = placement_vect_len / vector_length(parent.branch_vector)
			self.placement_vector = rotate_vector(parent.branch_vector * scale_factor, -self.isoceles_angle)

			plot_placement_vectors(axes, parent.start, parent.branch_vector * scale_factor,  -self.isoceles_angle)

		else:
			self.placement_vector = np.matrix( [[branch_length], [0]] )
