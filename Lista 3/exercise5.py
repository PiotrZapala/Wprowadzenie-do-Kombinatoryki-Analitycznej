import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f1(z):
    return np.abs(z)

def f2(z):
    return np.abs(z**2)

def f3(z):
    return 1 / (2 - np.exp(z))

def f4(z):
    return 1 / ((1 - z) * (1 - z/2) * (1 - z/3))

def f5(z):
    return (1 + z + z**2) / (1 - z - z**2 - z**3)

def f6(z):
    return np.exp(-z) / (2 - np.exp(z))

def f7(z):
    return np.sqrt(1 - 4*z)

def g(z, func):
    return np.abs(func(z))

z_real = np.linspace(0, 10, 400)
z_imag = np.linspace(0j, 10j, 400)
z_values_real, z_values_imag = np.meshgrid(z_real, z_imag)
z_values = z_values_real + z_values_imag
print(z_values_real)
functions = ["|z|", "|z^(2)|", "1/(2-e^(z))",
             "1/((1-z)(1-(z/2))(1-(z/3)))",
             "(1+z+z^(2))/(1-z-z^(2)-z^(3))",
             "e^(-z)/(2-e^(z))", "(1 - 4z)^(1/2)"]
func = [f1, f2, f3, f4, f5, f6, f7]
for i in range(len(func)):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    surface = ax.plot_surface(z_values_real, z_values_imag.imag, g(z_values, func[i]), cmap='viridis', edgecolor='k', linewidth=0.5)
    
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    
    ax.scatter([0], [0], [0], color='red', s=50)
    
    ax.text(0.1, 0.1, 0, '0', color='red', fontsize=8)
    
    fig.colorbar(surface, ax=ax, format='%.1f')
    
    ax.set_title(f'|f(z)| for f(z) = {functions[i]}')
    
    plt.show()
