import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# real image length: 1m ~ 10m (1000mm ~ 10000mm)
u = np.arange(1000, 10000, 100)

# focal length: 14mm ~ 140mm
f = np.arange(14, 141, 1)

# virtual image length: v = (u * f)/(u - f)
# ratio if u1 and u2: (v1 - f)/(v2 - f)
vfunc = np.vectorize(lambda u, f: (u*f/(u-f) -f) / ( ((u+1000)*f) / ((u+1000)-f) -f))

U, F = np.meshgrid(u, f)
R = vfunc(U, F)


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(U, F, R)
plt.show()
