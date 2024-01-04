import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(55, 250, 100)
y = np.linspace(0, 100, 100)

y2 = np.linspace(10,10,100)

X, Y = np.meshgrid(x, y)


Z = ((X - 55) * 0.5) * (1 + (Y - 10) / (90 * 0.5)) / 100


plt.contourf(X, Y, Z, cmap='jet', vmax=1.0, alpha=0.5, levels=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,1,999])

plt.plot(x, y2, label="Safe level")

plt.xlabel('Fuel temperature')
plt.ylabel('Core Outer Vessel Fill %')
plt.title('Core and Fuel integrity loss on extraction (10% per level)')


plt.savefig('img/fuel_level_safe_extraction_conditions.png')
