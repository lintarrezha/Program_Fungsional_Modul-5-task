import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8, 10])
ypoints = np.array([3, 10, 5])

plt.figure(figsize=(5, 5))

# plot dengan label sumbu, judul, warna, dan gaya garis
plt.plot(xpoints, ypoints, color='red', marker='o', label='Data Points')

# Batasan sumbu X dan Y
plt.xlim([0, 15])
plt.ylim([0, 15])

# label sumbu
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

plt.legend()

plt.show()
