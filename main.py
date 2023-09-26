import numpy as np
import matplotlib.pyplot as plt

# Запрашиваем у пользователя коэффициенты
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))
d = float(input("Введите коэффициент d: "))

# Генерация данных
x = np.linspace(-10, 10, 400)
y = a * x**3 + b * x**2 + c * x + d

# Визуализация
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=f'y = {a}x^3 + {b}x^2 + {c}x + {d}', color='blue')

# Настройка графика
plt.title("Кубическая парабола с системой координат")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)

# Добавляем оси координат
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.gca().spines['top'].set_position('zero')
plt.gca().spines['right'].set_position('zero')
plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines['left'].set_position('zero')

# Отображение графика
plt.show()
