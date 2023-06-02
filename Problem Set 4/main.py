import math
import UserInput as UI
import numpy as np
from numpy.polynomial.hermite import hermgauss

def calculateValueOfFunction(functionVariant, value):
    if functionVariant == 1:
        return np.sin(value)
    elif functionVariant == 2:
        return horner([1, 5, -4, -20], 4, value)
    elif functionVariant == 3:
        return np.cos(2*value)
    elif functionVariant == 4:
        return 2 * np.cos(2*value -1)
    else:
        print("Wrong function argument!!!")

def horner(tab, n, x):
    result = tab[0]
    for i in range(1, n):
        result = result * x + tab[i]
    return result

def weight_function(x):
    return math.exp(-x**2)

def newton_cotes_simpson(a, b, precision, functionVariant, numOfPartitionsPrint=False):
    n = 2

    prev_integral = 0
    integral = 0
    tmp = 0;

    while True:
        h = (b - a) / n
        x = [a + i * h for i in range(n+1)]

        integral = 0
        for i in range(n//2):
            integral += (h / 3) * (calculateValueOfFunction(functionVariant, x[2*i])
                                   + (4*calculateValueOfFunction(functionVariant, x[2*i+1]))
                                   + (calculateValueOfFunction(functionVariant, x[2*i+2])))
        if abs(integral - prev_integral) < precision:
            break

        prev_integral = integral
        n *= 2
        tmp+=1

    if numOfPartitionsPrint:
        print("Newton-cotes number of partitions:", tmp)

    return integral

def gauss_hermite_integration(functionVariant, n):
    x, w = hermgauss(n)
    f_values = calculateValueOfFunction(functionVariant, x)
    integral = np.dot(w, f_values)
    return integral

def calculateInfinityLimit(functionVariant, precision):
    a = 0
    b = 10
    add = 10;
    result = 0
    while True:
        prevIntegral = newton_cotes_simpson(a, b, precision, functionVariant)
        result += prevIntegral
        integral = newton_cotes_simpson(b, b+add, precision, functionVariant)
        if abs(integral) < precision:
            break
        a = b
        b += add
    return result

def calculateMinusInfinityLimit(functionVariant, precision):
    a = 0
    b = -10
    add = -10;
    result = 0
    while True:
        prevIntegral = newton_cotes_simpson(a, b, precision, functionVariant)
        result += prevIntegral
        integral = newton_cotes_simpson(b, b+add, precision, functionVariant)
        if abs(integral) < precision:
            break
        a = b
        b -= add
    return result

functionVariant = UI.printChooseFunctionMenu()
precision = UI.printChoosePrecisionMenu()
rangeVariant = UI.printChooseRangeVariantMenu()
if rangeVariant == 1:
    a = calculateInfinityLimit(functionVariant, precision)
    b = calculateMinusInfinityLimit(functionVariant, precision)
    numberOfNodes = UI.printChooseEnterNumberOfNodesMenu()
    print("----------------------------------------")
    print("RESULT")
    print("----------------------------------------")
    resultNewtonCotes = newton_cotes_simpson(a, b, precision, functionVariant, True)
    resultHermite = gauss_hermite_integration(functionVariant, numberOfNodes)
    print("Number of Hermite's nodes: ", numberOfNodes)
    print("Precision: ", precision)
    print("Range: (-∞ ; +∞)")
    print("Newton-Cotes:", resultNewtonCotes)
    print("Gauss-Hermite:", resultHermite)
if rangeVariant == 2:
    a, b = UI.printChooseRangeMenu()
    print("----------------------------------------")
    print("RESULT")
    print("----------------------------------------")
    resultNewtonCotes = newton_cotes_simpson(a, b, precision, functionVariant, True)
    print("Precision: ", precision)
    print("Range: [", a, " ; ", b,"]")
    print("Newton-Cotes:", resultNewtonCotes)