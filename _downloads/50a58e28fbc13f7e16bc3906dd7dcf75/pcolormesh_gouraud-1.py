import matplotlib.pyplot as plt
import numpy as np

nrows, ncols = 3, 5
Z = np.arange(nrows * ncols).reshape(nrows, ncols)
x = np.arange(ncols + 1)
y = np.arange(nrows + 1)

fig, axs = plt.subplots(2, 2, layout='constrained')

# Data at corners, requires X and Y the same shape as Z.
axs[0, 0].pcolormesh(x[:-1], y[:-1], Z, shading='nearest')
axs[0, 0].set_title('nearest: X, Y, Z same shape')

axs[0, 1].pcolormesh(x[:-1], y[:-1], Z, shading='gouraud')
axs[0, 1].set_title('gouraud: X, Y, Z same shape')

# Data at centers, requires X and Y one larger than Z.
axs[1, 0].pcolormesh(x, y, Z, shading='flat')
axs[1, 0].set_title('flat: X, Y one larger than Z')

axs[1, 1].pcolormesh(x, y, Z, shading='gouraud')
axs[1, 1].set_title('gouraud: X, Y one larger than Z')

plt.show()