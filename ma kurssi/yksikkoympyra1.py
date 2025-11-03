from matplotlib import pyplot as plt, patches
import numpy as np

fig, ax = plt.subplots()
ymp = patches.Circle((0, 0), radius=1, fill=False)
ax.add_patch(ymp)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.axis('equal')

plt.xticks([-1, 0, 1])
plt.yticks([-1, 0, 1])

angles_deg = np.array([30, 45, 60, 90, 120, 150, 180, 270])
angles_rad = np.deg2rad(angles_deg)

x = np.cos(angles_rad)
y = np.sin(angles_rad)

plt.scatter(x, y, color='red', marker='x')

for i in range(len(angles_deg)):
    plt.annotate(f"{angles_deg[i]}°",
                 (x[i], y[i]),
                 xytext=(10, 10),
                 textcoords='offset points',
                 fontsize=12,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

plt.title("Yksikköympyrä – merkityt kulmat 30°, 45°, 60°, 90°, 120°, 150°, 180°, 270°")
plt.show()
