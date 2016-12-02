import math
import numpy as np
import matplotlib.pyplot as plt

from branch_classes import Branch, Minimum_Branch
from utility_fxns import *


BRANCH_LENGTH = 4


def create_nuclear_family(possiblities, parent = None):

	minimum_branch = Minimum_Branch(ax, BRANCH_LENGTH, parent)
	if parent:
		ranger = 2 * minimum_branch.isoceles_angle
		sibling_increment = ranger / (len(possiblities) - 1) + ranger / 15

	else:
		sibling_increment = math.pi * 2 / len(possiblities)


	family = []
	for i, p in enumerate(possiblities):
		family.append(Branch(minimum_branch = minimum_branch, axes = ax, rotation = sibling_increment * i, 
			sibling_increment = sibling_increment, parent = parent, name = p))

	return family




fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
plt.axis([-15,15,-15,15])
plt.axis('off')


all_branches = []
top_level_branches = create_nuclear_family(['A',1,1])
all_branches.extend(top_level_branches)
ax.plot([0],[0], 'bo', markersize = 20)

for tlb in top_level_branches:
	a = create_nuclear_family(['A', 'B', 'C','d'], tlb)
	all_branches.extend(a)
	for aa in a:
		b = create_nuclear_family([1,2,3], aa)
		all_branches.extend(b)

for b in all_branches:
	b.label_branch()
plt.pause(10)

