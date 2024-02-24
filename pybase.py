import matplotlib.pyplot as plt
import numpy as np

N = 201  # no of terms
tt = np.linspace(-1,1,N)
xx, yy = np.meshgrid(tt, tt)
rr = np.hypot(xx, yy)
II = np.zeros((N,N))

a1 = np.where(rr <= 1.)
a2 = np.where(rr <= 0.8)
a3 = np.where(rr <= 0.6)
a4 = np.where(rr <= 0.4)
a5 = np.where(rr <= 0.2)

II[a1] = 1
II[a2] = 2
II[a3] = 3
II[a4] = 4
II[a5] = 5

plt.imshow(II, extent=[-1, 1, -1, 1], origin='lower')
plt.show()