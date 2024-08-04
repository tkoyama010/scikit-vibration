import numpy as np
import matplotlib.pyplot as plt

# System parameters
modes = [1, 2]  # Number of modes
frequencies = [10, 20]  # Natural frequencies (Hz)
damping_ratios = [0.05, 0.02]  # Loss factors
residues = [1.0, 0.8]  # Residues

# Frequency range
frequencies_range = np.linspace(0, 30, 1000)
omega = 2 * np.pi * frequencies_range

# Compute FRF
H = np.zeros(len(omega), dtype=complex)

for i in range(len(modes)):
    omega_i = 2 * np.pi * frequencies[i]
    eta_i = damping_ratios[i]
    R_i = residues[i]
    # Compute the FRF for each mode and sum them
    H += R_i / (1j * omega - omega_i * (1 - 1j * eta_i)) + R_i / (1j * omega + omega_i * (1 + 1j * eta_i))

# Compute magnitude and phase of the FRF
magnitude = np.abs(H)
phase = np.angle(H)

# Plotting
plt.figure(figsize=(12, 6))

# Magnitude plot
plt.subplot(2, 1, 1)
plt.plot(frequencies_range, magnitude)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Response Function (Magnitude)')

# Phase plot
plt.subplot(2, 1, 2)
plt.plot(frequencies_range, phase)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (radians)')
plt.title('Frequency Response Function (Phase)')

plt.tight_layout()
plt.show()
