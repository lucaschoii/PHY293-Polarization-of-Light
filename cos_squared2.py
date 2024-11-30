import numpy as np
import matplotlib.pyplot as plt
from lmfit import Model

xlabel = 'cos$^{2}(θ)$'
ylabel = 'Light Intensity [V]'
title = 'Light Intensity [V] vs cos$^{2}(θ)$'


def sine_squared(x, a, k, psi, b):
    return a * np.sin(k * x + psi)**2 + b

# Load data
file_path = 'data/2/processed/cos2x1.txt'
data = np.loadtxt(file_path, skiprows=1)  
x = data[:, 0]
y = data[:, 1]
dx = data[:, 2]
dy = data[:, 3]

# Fit the data
exercise_2_model = Model(sine_squared)
params = exercise_2_model.make_params(a=max(y), k=1, psi=0, b=0)
result = exercise_2_model.fit(y, params, x=x, xerr=dx, yerr=dy)

# Extract the fitted parameters
a_fit = result.params['a'].value
k_fit = result.params['k'].value
psi_fit = result.params['psi'].value
b_fit = result.params['b'].value

# Calculate residuals
residuals = y - result.eval(x=x)

# Plot
x_fine = np.linspace(min(x), max(x), 500)
fitted_y = sine_squared(x_fine, a_fit, k_fit, psi_fit, b_fit)
fig, (ax_main, ax_residuals) = plt.subplots(2, 1, figsize=(10, 8), gridspec_kw={'height_ratios': [3, 1]}, sharex=True)

# Main plot: Data and fit
ax_main.errorbar(
    x,
    y,
    yerr=dy,
    xerr=dx,
    fmt='o',          
    markersize=2,      
    label='Experimental Data',
    color='blue',
    capsize=3          
)

ax_main.plot(x_fine, fitted_y, '-', 
             label=f'Fit: $I = a \\cos^2(k  \\theta + \\psi) + b$', 
             color='red')

ax_main.set_title(title, fontsize=14)
ax_main.set_ylabel(ylabel, fontsize=12)
ax_main.grid(True, linestyle='--', alpha=0.7)
ax_main.legend()

# Residuals plot
ax_residuals.errorbar(
    x,
    residuals,
    yerr=dy,
    xerr=dx,
    fmt='o',          
    markersize=2,      
    color='purple',
    capsize=3          
)
ax_residuals.axhline(0, color='black', linestyle='--', linewidth=1)
ax_residuals.set_xlabel(xlabel, fontsize=12)
ax_residuals.set_ylabel('Residuals', fontsize=12)
ax_residuals.grid(True, linestyle='--', alpha=0.7)

# Show the plots
plt.tight_layout()
print(result.fit_report())
plt.show()
