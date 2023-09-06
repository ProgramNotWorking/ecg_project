import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.plot(x, y, color='white', linewidth=3.0)
plt.xlabel('Time', color='white')
plt.ylabel('Amplitude', color='white')
plt.xticks(color='white')
plt.yticks(color='white')
plt.title('ECG', color='white')
plt.grid(False)

ax = plt.gca()
ax.spines['top'].set_color('white')
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['right'].set_color('white')

plt.savefig(
    '/home/nikita/Изображения/Something/something_v6.png',
    transparent=True,
    bbox_inches='tight',
    pad_inches=0.1
)

plt.show()
