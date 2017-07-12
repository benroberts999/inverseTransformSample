import random
import math

# Generate randomly distributed angles:
# Uses uniform distribution [0,2pi] for phi, 
# and inverse transform sampling for theta.
num_points=150
phi_lst = [random.uniform(0,2*math.pi) for _ in range (num_points)]
u_lst = [random.uniform(0,1) for _ in range (num_points)]
theta_lst=[math.acos(1-2*u_lst[i]) for i in range (num_points)]

# Define cartesian coordinates:
def x(i):
    return math.sin(theta_lst[i])*math.cos(phi_lst[i])
def y(i):
    return math.sin(theta_lst[i])*math.sin(phi_lst[i])
def z(i):
    return math.cos(theta_lst[i])
xyz_lst=[(x(i),y(i),z(i)) for i in range (num_points)]

for i in range (num_points):
	print x(i), y(i), z(i)
