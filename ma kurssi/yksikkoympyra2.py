import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3*np.pi, 3*np.pi, 500)

y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(19.2, 4.8))

plt.plot(x, y1, color='crimson', linestyle='--', linewidth=2, label='sin(x)')
plt.plot(x, y2, color='royalblue', linestyle='-.', linewidth=2, label='cos(x)')

plt.title("Sin ja Cos -funktiot välillä -3π ... 3π", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.grid(True)

plt.legend(loc='upper right', fontsize=12)

plt.show()
