import random
import math
# Import the inverse error function from scipy:
from scipy.special import erfinv

# Generates random points (x_lst), that are drawn from Gaussian Distribution
# u_lst is the uniform distribution [0,1]
num_points=5000
x0=5.   # example centre for Gaussian
sd=1.5  # example standard deviation for Gaussian
u_lst = [random.uniform(0,1) for _ in range (num_points)]
x_lst = [(x0+math.sqrt(2.)*sd*erfinv(2*u_lst[i]-1)) for i in range (num_points)]

for i in range (num_points):
	print x_lst[i]
