import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.hermite import hermgauss
import UserInput as UI

def calculateValueOfFunction(functionVariant, value):
    if functionVariant == 1:
        return (3 * value) + 5
    elif functionVariant == 2:
        return np.abs(value)
    elif functionVariant == 3:
        return horner([2, 1, -2], 3, value)
    elif functionVariant == 4:
        return np.sin(value)
    elif functionVariant == 5:
        return np.cos(2 * (value**2) + 1)
    else:
        print("Wrong function argument!!!")

def horner(tab, n, x):
    result = tab[0]
    for i in range(1, n):
        result = result * x + tab[i]
    return result

def calculateError(functionVariant, nodes, result_coefficients):
    diff = 0
    for i in range(0, nodes.size):
        diff += np.abs(np.abs(calculateValueOfFunction(functionVariant, nodes[i])) - np.abs(
            horner(result_coefficients, result_coefficients.size, nodes[i])))
    return diff

def gauss_hermite_approximation(functionVariant, a, b, degree, n, isByError = False, errorTarget = 1):

    x, w = hermgauss(n)
    f_values = calculateValueOfFunction(functionVariant, x)
    x_approx = np.linspace(a, b, 100)
    f_approx = calculateValueOfFunction(functionVariant, x_approx)

    if isByError == False:
        result_coefficients = np.polyfit(x, f_values, degree)
        p_approx = np.polyval(result_coefficients, x_approx)
        error = calculateError(functionVariant, x, result_coefficients)
    else:
        errorReached = False;
        while errorReached == False:
            result_coefficients = np.polyfit(x, f_values, degree)
            p_approx = np.polyval(result_coefficients, x_approx)
            error = calculateError(functionVariant, x, result_coefficients)
            if error <= errorTarget:
                errorReached = True
            degree += 1

    plt.plot(x_approx, f_approx, label='Original Function')
    plt.plot(x_approx, p_approx, label='Approximation')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Function Approximation')
    formatted_number = f"{error:.16f}"
    print("Approximation error:", formatted_number)
    np.set_printoptions(precision=4, suppress=True)
    print("Approximation coefficients :", result_coefficients)
    plt.show()

function_variant = UI.printChooseFunctionMenu()
variant = UI.printChooseApproximationVariant()
a, b = UI.printChooseRangeMenu()
n = UI.printChooseEnterNumberOfNodesMenu()
if variant == 1:
    degree = UI.printChooseEnterPolynomialDegree()
    gauss_hermite_approximation(function_variant, a, b, degree, n)
elif variant == 2:
    error = UI.printChooseApproximationError()
    gauss_hermite_approximation(function_variant, a, b, 1, n, True, error)