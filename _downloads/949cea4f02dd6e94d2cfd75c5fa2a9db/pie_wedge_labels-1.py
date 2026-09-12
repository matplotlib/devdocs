import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(ncols=2, layout='constrained')

ax1.pie([1, 2], wedge_labels=['foo', 'bar'], wedge_label_distance=1.1)
ax2.pie([1, 2], wedge_labels='{absval:d}', wedge_label_distance=0.6)