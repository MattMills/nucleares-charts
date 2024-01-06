import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator

# Define the functions
def absorption_factor(model_position, integrity, active_bars):
    # Assuming absorption_factor is calculated using the provided logic
    pos_effect = positive_effect(model_position, integrity, active_bars)
    return 1 - (pos_effect / 100)

def moderation_factor(moderation):
    # Assuming moderation_factor is a linear function between 0.2 and 1.0
    return 0.2 + 0.8 * moderation

# Generate random data for demonstration
fuel_qty_values = np.linspace(0, 30240, 100)
absorption_factors = np.linspace(0.0, 1.0, 100)
moderation_factors = np.linspace(0.2, 1.0, 100)

# Create a grid of fuel_qty, absorption_factor, and moderation_factor values
absorption_grid, moderation_grid = np.meshgrid(absorption_factors, moderation_factors)

# Calculate the expression values for the generated data
expression_values = np.maximum(0.01, np.round(180 * 30240 / 30240, 2)) * absorption_grid * moderation_grid

# Create a 3D scatter plot
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')


# Plot the scatter plot
#ax.plot_surface(absorption_grid, moderation_grid, expression_flat)
#ax.scatter(absorption_grid, moderation_grid, expression_values, cmap='viridis', alpha=0.8)
levels = np.linspace(expression_values.min(), expression_values.max(), 100)
plt.contourf(absorption_grid,moderation_grid,expression_values, cmap='jet', levels=levels)

# Add a colorbar which maps values to colors
#ax.zaxis.set_major_locator(LinearLocator(10))

# Set labels and title
plt.xlabel('Absorption (Inverted)')
plt.ylabel('Moderation')
plt.title('Fission reactivity tick calculation')
plt.colorbar(label='Temperature increase')




plt.savefig('img/reactivity.png')
