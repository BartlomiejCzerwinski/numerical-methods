import math
import scipy.integrate as spi

def calculateValueOfFunction(functionVariant, value):
    if functionVariant == 1:
        return horner([5, -2], 2, value)
    elif functionVariant == 2:
        return horner([1, 5, -4, -20], 4, value)
    elif functionVariant == 3:
        return math.sin(value)
    else:
        print("Wrong function argument!!!")

def horner(tab, n, x):
    result = tab[0]
    for i in range(1, n):
        result = result * x + tab[i]
    return result

def weight_function(x):
    return math.exp(-x**2)

def newton_cotes_simpson(a, b, precision, functionVariant):
    n = 2

    prev_integral = 0
    integral = 0
    tmp = 0;

    while True:
        h = (b - a) / n
        x = [a + i * h for i in range(n+1)]

        integral = 0
        for i in range(n//2):
            integral += (h / 3) * (weight_function(x[2*i])*calculateValueOfFunction(functionVariant, x[2*i])
                                   + (weight_function(x[2*i+1])*4*calculateValueOfFunction(functionVariant, x[2*i+1]))
                                   + (weight_function(x[2*i+2])*calculateValueOfFunction(functionVariant, x[2*i+2])))
        if abs(integral - prev_integral) < precision:
            break

        prev_integral = integral
        n *= 2
        tmp+=1
    print(tmp)

    return integral

def gauss_integration(f, a, b, precision):
    result, _ = spi.quad(f, a, b, epsabs=precision)
    return result

def f(x):
    return math.exp(-x**2) * calculateValueOfFunction(1, x)

a = 2
b = 10
precision = 0.001

result_gauss = gauss_integration(f, -math.inf, math.inf, precision)
print("Gauss:", result_gauss)

a = 2
b = 10
precision = 0.001

result = newton_cotes_simpson(a, b, precision, 1)
print("Newtona-Cotes:", result)
