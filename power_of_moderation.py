import numpy as np
import matplotlib.pyplot as plt

# Define the function
def custom_function(x, y):
    return np.minimum(100,np.maximum(20, np.clip(x / (x + y), 0, 1) * 100 * (x / 120000)))

# Generate x and y values
x_values = np.linspace(0, 120000, 1000)
y_values = np.linspace(0, 120000, 1000)

# Create a grid of x and y values
x, y = np.meshgrid(x_values, y_values)

# Calculate corresponding z values using the custom function
z_values = custom_function(x, y)

# Plot the function using a contour plot
plt.contourf(x, y, z_values, cmap='viridis')
plt.colorbar(label='Power of Moderation')
plt.xlabel('Water')
plt.ylabel('Steam')
plt.title('Power of Moderation')
plt.savefig('img/power_of_moderation.png')
