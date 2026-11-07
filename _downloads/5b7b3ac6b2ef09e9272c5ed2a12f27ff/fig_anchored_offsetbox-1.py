import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.offsetbox import AnchoredText, AnchoredOffsetbox, DrawingArea

fig = plt.figure()

sfig1, sfig2 = fig.subfigures(ncols=2)
sfig1.set_facecolor("lemonchiffon")
sfig2.set_facecolor("lightcyan")

fig_text = AnchoredText("Anchored to Figure", loc="upper left")
fig.add_artist(fig_text)

sfig_text = AnchoredText("Anchored to SubFigure", loc="lower right")
sfig1.add_artist(sfig_text)

area = DrawingArea(width=30, height=30)
area.add_artist(mpatches.Circle((15, 15), 15, fc="tab:blue"))
box = AnchoredOffsetbox(child=area, loc="center left")
sfig2.add_artist(box)