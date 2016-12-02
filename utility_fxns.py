import math
import numpy as np
import matplotlib.pyplot as plt

def vector_length(vector):
	return (vector.flat[0] ** 2 + vector.flat[1] ** 2) ** (1 / 2)



def plot_placement_vectors(ax, start, vector, rotation):

	rotation_increments = 15
	r = 0
	while True:
		
		if abs(r) > abs(rotation) - abs(rotation) / (rotation_increments + 1):
			
			for alpha in np.arange(1,0,-0.2):
				final_line, = plot_vector(ax, start, vector, alpha = alpha, color = 'g', linestyle = '--', linewidth = 5)
				preliminary_dot, = ax.plot([start[0] + vector.flat[0]], [start[1] + vector.flat[1]], 'bo')
				plt.pause(0.005)
				final_line.remove()
				preliminary_dot.remove()
			break

		else:
			vector = rotate_vector(vector, rotation / rotation_increments)
			transient_line, = plot_vector(ax, start, vector, alpha = 0.5, color = '#003300', linestyle = '--' )
			plt.pause(0.000001) # at a certain point, pause won't get any smaller
			transient_line.remove()
			r += rotation / rotation_increments



def plot_vector(ax, start, vector, alpha = 1, color = 'r', linestyle = '-', linewidth = 2):
	end = vector.flat[0] + start[0], vector.flat[1] + start[1]
	return ax.plot([start[0], end[0]], [start[1], end[1]], alpha = alpha, color = color, linestyle = linestyle, linewidth = linewidth)





def rotate_vector(vector, rotation_theta):
	rotation_matrix = np.matrix([ [math.cos(rotation_theta), -math.sin(rotation_theta)], [math.sin(rotation_theta), math.cos(rotation_theta)] ])
	return np.dot(rotation_matrix, vector)
