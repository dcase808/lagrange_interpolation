import sympy as sp
import matplotlib.pyplot as plt

def lagrange (x_array, y_array):
    x = sp.symbols('x')
    result = 0
    for i in range(len(x_array)):
        temp = 1
        for j in range(len(x_array)):
            if j != i:
                temp *= ((x - x_array[j]) / (x_array[i] - x_array[j]))
        result += temp * y_array[i]
    return sp.simplify(result)


x_array = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1]
y_array = [18.559624, 22.000392, 25.925000, 30.007048, 33.505416, 31.895624]


result = lagrange(x_array, y_array)
print(result)

x = sp.symbols("x")
sp.plot(result, (x, 0.1, 1.1))
