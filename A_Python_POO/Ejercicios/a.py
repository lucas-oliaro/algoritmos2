import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Parámetros de la distribución
mu = 5
sigma = 0.5
c = 0.8225

# Crear un rango de valores para la distribución normal
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = stats.norm.pdf(x, mu, sigma)

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Distribución Normal', color='blue')

# Área del intervalo de confianza
x_fill = np.linspace(mu - c, mu + c, 1000)
y_fill = stats.norm.pdf(x_fill, mu, sigma)
plt.fill_between(x_fill, y_fill, color='lightblue', alpha=0.5, label='Intervalo del 90%')

# Agregar líneas verticales para los límites del intervalo
plt.axvline(mu - c, color='red', linestyle='--', label=f'Límite inferior ({mu - c:.2f})')
plt.axvline(mu + c, color='red', linestyle='--', label=f'Límite superior ({mu + c:.2f})')

# Etiquetas y título
plt.title('Distribución Normal con Intervalo de Confianza del 90%')
plt.xlabel('Valor de X')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()
