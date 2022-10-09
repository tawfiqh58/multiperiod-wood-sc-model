import matplotlib.pyplot as plt 
import numpy as np 

# Generate pseudo-random numbers:
np.random.seed(0) 

# Sampling interval:    
dt = 0.01 

# Sampling Frequency:
Fs = 1 / dt  # ex[;aom Fs] 

# Generate noise:
t = np.arange(0, 10, dt) 
res = np.random.randn(len(t)) 
r = np.exp(-t / 0.05) 

# Convolve 2 signals (functions):
conv_res = np.convolve(res, r)*dt
conv_res = conv_res[:len(t)] 
s = 0.5 * np.sin(1.5 * np.pi * t) + conv_res

# Create the plot: 
fig, (ax) = plt.subplots() 
ax.plot(t, s) 
# Function plots phase spectrum:
ax.phase_spectrum(s, Fs = Fs)

plt.title("Phase Spectrum Plot")
plt.show()