import numpy as np
import matplotlib.pyplot as plt

# Создаем набор точек
x1 = np.array([0, 276.6, 221.36, 174.2, 150.68, 123.72, 108.01, 85.52, 67.51, 46.44, 31.57, 27.89, 23.13])
y1 = np.array([0, 585, 467.5, 367.5, 320, 260, 230, 180, 142.5, 97.5, 65, 60, 47.5])

# Выполняем аппроксимацию методом наименьших квадратов
coefficients = np.polyfit(x1, y1, 1)  # Линейная аппроксимация
slope = coefficients[0]
print(slope)
poly_fit = np.poly1d(coefficients)

# Создаем сетчатое поле
plt.figure(figsize=(8, 8))
plt.grid(True)

# Строим точки
plt.scatter(x1, y1, label='Точки', color='red')

# Строим аппроксимацию
x_values = np.linspace(min(x1), max(x1), 100)
y_values = poly_fit(x_values)
plt.plot(x_values, y_values, label='L = 20cm', linestyle='-')

x2 = np.array([0, 229.81, 191.03, 158.67, 144.10, 125.02, 109.39, 95.37, 84.59, 70.16, 59.35, 50.76, 26.784])
y2 = np.array([0, 697.5, 600, 500, 452.5, 395, 345, 300, 265, 222.5, 185, 160, 85])

coefficients = np.polyfit(x2, y2, 1) 
slope = coefficients[0]
print(slope)
poly_fit = np.poly1d(coefficients)

plt.scatter(x2, y2, color='red')

x_values = np.linspace(min(x2), max(x2), 100)
y_values = poly_fit(x_values)
plt.plot(x_values, y_values, label='L = 30cm', linestyle='-')

x3 = np.array([0, 137.21, 93.46, 80.52, 67.24, 59.79, 52.04, 46.31, 31.312, 28.762, 26.783, 22.099])
y3 = np.array([0, 710, 482.5, 415, 347.5, 310, 270, 240, 160, 147.5, 137.5, 115])

coefficients = np.polyfit(x3, y3, 1) 
slope = coefficients[0]
print(slope)
poly_fit = np.poly1d(coefficients)

plt.scatter(x3, y3, color='red')

x_values = np.linspace(min(x3), max(x3), 100)
y_values = poly_fit(x_values)
plt.plot(x_values, y_values, label='L = 50cm', linestyle='-')

# Добавляем легенду
plt.legend()

# Добавляем подписи к осям
plt.xlabel('I, mA')
plt.ylabel('U, mB')

# Отображаем график
plt.show()