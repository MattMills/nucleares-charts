import numpy as np
import matplotlib.pyplot as plt

def integrity_factor(integrity):
    if 50 <= integrity < 80:
        return 0.99
    elif 30 <= integrity < 50:
        return 0.98
    elif integrity < 30:
        return 0.96
    else:
        return 1

def quantity_factor(active_bars):
    total_bars = 8.0
    return active_bars / total_bars

def positive_effect(model_position, integrity, active_bars):
    int_factor = integrity_factor(integrity)
    quant_factor = quantity_factor(active_bars)
    return ((model_position) * int_factor * quant_factor)

def absorption_factor(model_position, integrity, active_bars):
    pos_effect = positive_effect(model_position, integrity, active_bars)
    return 1 - (pos_effect / 100)


# Generate linear values for model_positions and integrities
model_positions = np.linspace(100, 0, 100)
integrities = np.linspace(0, 100, 100)
active_bars = 8.0  # Use 8 active bars for all data points

# Create a grid of model_positions and integrities
model_positions_grid, integrities_grid = np.meshgrid(model_positions, integrities)

# Calculate absorption factors for the generated data
absorption_factors = np.zeros_like(model_positions_grid)
for i in range(len(model_positions)):
    for j in range(len(integrities)):
        absorption_factors[j, i] = absorption_factor(model_positions[i], integrities[j], active_bars)

# Plot the contour plot
plt.contourf(integrities_grid, model_positions_grid, absorption_factors, cmap='viridis', levels=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
plt.colorbar(label='Absorption Factor')
plt.xlabel('Control Bars Integrity')
plt.ylabel('Control Bars Height')
plt.title('Absorption Factor Contour Plot')

plt.savefig('img/absorption_factor.png')
