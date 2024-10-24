# Use old pcolormesh snapping values
plt.rcParams['pcolormesh.snap'] = False
fig, ax = plt.subplots()
xx, yy = np.meshgrid(np.arange(10), np.arange(10))
z = (xx + 1) * (yy + 1)
mesh = ax.pcolormesh(xx, yy, z, shading='auto', alpha=0.5)
fig.colorbar(mesh, orientation='vertical')
ax.set_title('Before (pcolormesh.snap = False)')