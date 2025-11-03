import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3*np.pi, 3*np.pi, 1000)

y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(19.2, 4.8))

plt.plot(x, y1, color='crimson', linestyle='--', linewidth=2, label='sin(x)')
plt.plot(x, y2, color='royalblue', linestyle='-.', linewidth=2, label='cos(x)')

plt.title("Sin ja Cos -funktiot välillä -3π ... 3π", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.grid(True, linestyle=':')

plt.xlim(-3*np.pi, 3*np.pi)
plt.ylim(-1.2, 1.2)

xticks = np.array([-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3]) * np.pi
xtick_labels = [
    r'$-3\pi$', r'$-\frac{5\pi}{2}$', r'$-2\pi$', r'$-\frac{3\pi}{2}$',
    r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$',
    r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$', r'$\frac{5\pi}{2}$', r'$3\pi$'
]
plt.xticks(xticks, xtick_labels, fontsize=11)

plt.legend(loc='upper right', fontsize=12)

plt.show()
