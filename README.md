# Randomly sample points with a uniform distribution over a sphere

Simple python code to randomly sample points with a uniform distribution over a sphere.
Makes use of inverse transform sampling.

**Inverse transform sampling:**
We want to randomly sample points from a given distribution, p(x).
What I mean by this, is that if I histogram the points that I sample, they histogram should match the p(x) distribution.
To do this, define:

C(x) = Integrate p(x') dx' ; -Infinity to x

let g(u) = C^-1(u)    [C^-1 is the inverse of C, NOT 1/C !]

If we then have a set of uniformly samped points {u},
the set {g(u)} will follow the probability distribution set by p(x)!

In our case, the probability distributions we want is the spherical solid-angle volume element

dV = sin(theta) d theta  d phi

[I am using convention where theta goes 0 -> Pi, phi goes 0 -> 2 Pi]

So, we should sample phi from a uniform distribution, but we should sample theta accoring to sin(theta)

p(theta) = sin(theta)

C(theta) = 1 - cos(theta)

g(u) = arccos(1 - 2u)

u: sampled uniformly from [0,1]

theta=g(u) : sampled according to p(theta)

**Usage:**
e.g., to place the output in a text file (that can be read by a plotting program):

python randUniSphere.py >> test.out
