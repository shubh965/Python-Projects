import numpy as np
import matplotlib.pyplot as plt

v = float(input("Enter the velocity with which projectile is thrown (in m/s) :"))
theta = float(input("Enter the angle from horizontal (in degree):"))
g = 9.81

A = np.radians(theta)
t = np.linspace(0, 2 * v * np.sin(A) / g, 100)
x = v * np.cos(A) * t
y = v * np.sin(A) * t - 0.5 * g * t ** 2

print("\nRange of the projectile:", f"{x[-1]:.2f}", "m")
print("Maximum Height of the Projectile:", f"{np.median(y):.2f}", "m")
print("The Time Taken by the Projectile is:", f"{t[-1]:.2f}", "s\n")

plt.plot(x, y)
plt.title("Projectile Motion")
plt.xlabel("Distance (m) ------->")
plt.ylabel("Height (m) ------->")
plt.xlim(0, max(x[-1], y[-1]) + 1)
plt.ylim(0, max(x[-1], y[-1]) / 2 + 1)
plt.grid(True)
plt.gca().set_aspect("equal", adjustable="box")
plt.show()
