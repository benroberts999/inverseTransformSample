

# Generate random variables drawn from a given PDF using Inverse Transform sampling

Two small python scritps showing examples of using inverse transform sampling to draw random points
accoring to a given probability distribution.

This is useful, for example, for performing Monte Carlo integrations.

First example is randomly placing points across the surphace of a sphere.
Other example is drawing from a Gaussian distribution.

Also, the same thing is done using Mathematica.
The Mathematica notebook will also plot the output of the python script.
Mathematica is proprotry software, so without a licence, you cannot run the notebook.
However, you can download the free "CDF player", which will allow you to see the formatted contents of the notebook (though won't let you run the code). It can be downloaded here:  
http://www.wolfram.com/cdf-player/  


### Randomly sample points with a uniform distribution over a sphere

Simple python code (also Mathematica) to randomly sample points with a uniform distribution over a sphere.
Makes use of inverse transform sampling.


**Usage:**

e.g., to place the output in a text file (that can be read by a plotting program):

$ python randUniSphere.py >> sphere.out

It uses 150 points, this is hard-coded in, but can be changed simply.  


### Randomly sample points drawn from a Gaussian

Simple python code (also Mathematica) to randomly sample points that match the probability distribution of a Gaussian.
Makes use of inverse transform sampling.


**Usage:**

e.g., to place the output in a text file (that can be read by a plotting program):

$ python sampleFromGaussian.py >> test.out

It uses 150 points, this is hard-coded in, but can be changed simply.  


## Inverse transform sampling:

We want to randomly sample points from a given distribution, p(x).
What I mean by this, is that if I histogram the points that I sample, they histogram should match the p(x) distribution.
To do this, define:

C(x) = Integrate p(x') dx' ; -Infinity -> x

let g(u) = C^-1(u)    [C^-1 is the inverse of C, not 1/C !]  


If we then have a set of uniformly samped points {u},
the set {g(u)} will follow the probability distribution set by p(x)!  


In our first case, as an example, the probability distributions we want is the spherical solid-angle volume element

dV = sin(theta) d theta  d phi

[I am using convention where theta goes 0 -> Pi, phi goes 0 -> 2 Pi]

So, we should sample phi from a uniform distribution, but we should sample theta accoring to sin(theta)

p(theta) = sin(theta)

C(theta) = 1 - cos(theta)

g(u) = arccos(1 - 2u)

u: sampled uniformly from [0,1]

theta=g(u) : sampled according to p(theta)

