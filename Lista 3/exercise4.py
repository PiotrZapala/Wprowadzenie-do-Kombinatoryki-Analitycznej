import numpy as np
import matplotlib.pyplot as plt

def surf1(r, t):
    x = np.real(r * np.exp(1j * t))
    y = np.imag(r * np.exp(1j * t))
    z = np.real(np.sqrt(r) * np.exp(1j * t / 2))
    return x, y, z

def surf2(r, t):
    x = np.real(r * np.exp(1j * t))
    y = np.imag(r * np.exp(1j * t))
    z = np.imag(np.sqrt(r) * np.exp(1j * t / 2))
    return x, y, z

def surf3(r, t):
    x = np.real(r * np.exp(1j * t))
    y = np.imag(r * np.exp(1j * t))
    z = np.abs(np.log(r) + 1j * t)
    return x, y, z


r_values = np.linspace(0, 1, 100)
t_values = np.linspace(0, 4 * np.pi, 100)

r_values_3 = np.linspace(0.1, 10, 100)
t_values_3 = np.linspace(0, 8 * np.pi, 100)

fig = plt.figure(figsize=(18, 6))

ax1 = fig.add_subplot(131, projection='3d')
X1, Y1, Z1 = surf1(*np.meshgrid(r_values, t_values))
ax1.plot_surface(X1, Y1, Z1, cmap='Greens', edgecolor='k')
ax1.set_title('Sr')

ax2 = fig.add_subplot(132, projection='3d')
X2, Y2, Z2 = surf2(*np.meshgrid(r_values, t_values))
ax2.plot_surface(X2, Y2, Z2, cmap='Greens', edgecolor='k')
ax2.set_title('Sc')

ax3 = fig.add_subplot(133, projection='3d')
X3, Y3, Z3 = surf3(*np.meshgrid(r_values_3, t_values_3))
ax3.plot_surface(X3, Y3, Z3, cmap='Greens', edgecolor='k')
ax3.set_title('L')

plt.show()
