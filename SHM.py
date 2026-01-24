import numpy as np
import matplotlib.pyplot as plt

A = float(input("Enter the Amplitude for the SHM (in m) :"))
omega = float(input("Enter the angular frequency (in rad/s) :"))
print()
t = np.linspace(0, 2 * np.pi, 300)

x = A * np.sin(omega * t)

plt.plot(t, x)
plt.title("Simple Harmonic Motion")
plt.xlim(0, 2 * np.pi)
plt.ylim(-A - 0.1, A + 0.5)
plt.xlabel("Time (s) ------->")
plt.ylabel("Position (m) ------->")
ticks = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
labels = ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$']
plt.xticks(ticks, labels)
plt.grid()
plt.show()
