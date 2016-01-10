import math
import matplotlib.pyplot as plt
import numpy as np

#Initial conditions

x = 0.01
pc = 0.1

xlist = []
qlist = []
plist = []
flist = []
tlist = []

dt = 0.01
nsteps = 1000

for i in range(nsteps):
    xlist.append(x)
    x += 1

q = (pc*x**3)/3

p = pc - (pc**2*x**2)/6

f = (pc**2*x**3)/3

t = 1 - (pc**4*x**4)/6


#Transformed differential equations

dq = (p*t**2)/t

dp = -(p*q)/(t*x**2)

df = p**2*t**2*x**2

dt = -(p**2*f)/(t**8.5*x**2)

#Integration
#Use Euler integration

for i in enumerate(xlist):
    q += dt*dq
    qlist.append(q)

    p += dt*dp
    plist.append(p)

    f += dt*df
    flist.append(f)

    t += dt*dt
    tlist.append(t)

plt.plot(x, q)
plt.plot(x, p)
plt.plot(x, f)
plt.plot(x, t)
plt.show()

#Left off trying to figure out the problem with raising negative number to fractional expontent
