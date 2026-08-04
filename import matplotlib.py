import matplotlib.pyplot as plt
import numpy as np

# Create random peak lengths for the waveform
np.random.seed(42)
num_bars = 80
bar_lengths = np.random.uniform(0.1, 1.0, num_bars)

# Smooth out the lengths to make it look like a real wave
smoothed_lengths = np.convolve(bar_lengths, np.ones(5)/5, mode='same')

# Set up a dark background plot
fig, ax = plt.subplots(figsize=(2, 10), facecolor='black')
ax.set_facecolor('black')

# Plot each line horizontally centered vertically
y_positions = np.arange(num_bars)
for y, length in zip(y_positions, smoothed_lengths):
    # Draw horizontal bars centered at x=0
    ax.plot([-length, length], [y, y], color='white', solid_capstyle='round', linewidth=3)

# Clean up axes
ax.axis('off')
plt.show()
