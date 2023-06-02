import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.hermite import hermgauss

def calculateValueOfFunction(functionVariant, value):
    if functionVariant == 1:
        return horner([1, 0, 3], 3, value)
    elif functionVariant == 2:
        return horner([1, 5, -4, -20], 4, value)
    elif functionVariant == 3:
        return np.cos(2 * value)
    elif functionVariant == 4:
        return 2 * np.cos(2 * value - 1)
    else:
        print("Wrong function argument!!!")

def horner(tab, n, x):
    result = tab[0]
    for i in range(1, n):
        result = result * x + tab[i]
    return result

def gauss_hermite_integration(functionVariant, a, b, degree, n):
    x, w = hermgauss(n)
    f_values = calculateValueOfFunction(functionVariant, x)
    integral = np.dot(w, f_values)

    x_approx = np.linspace(a, b, 100)
    f_approx = calculateValueOfFunction(functionVariant, x_approx)
    p_coefficients = np.polyfit(x, f_values, degree)
    p_approx = np.polyval(p_coefficients, x_approx)

    plt.plot(x_approx, f_approx, label='Original Function')
    plt.plot(x_approx, p_approx, label='Approximation')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Function Approximation')
    plt.show()

    return integral


function_variant = 1
a = -5
b = 5
degree = 2
n = 5

integral_value = gauss_hermite_integration(function_variant, a, b, degree, n)
print("Approximate integral value:", integral_value)
