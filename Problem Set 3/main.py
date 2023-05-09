import numpy as np
import matplotlib.pyplot as plt
import math
import UserInput as UI

def calculate_interpolated_values(y, xi, nodes):
    n = len(nodes)
    c = newton_interpolation(nodes, y)
    yi = []
    for x_val in xi:
        L = np.ones(n)
        for i in range(1, n):
            L[i] = L[i-1] * (x_val - nodes[i-1])
        yi.append(np.sum(c * L))
    return yi

def calculateValueOfFunction(functionVariant, value):
    if functionVariant == 1:
        return (5 * value) - 2
    elif functionVariant == 2:
        return abs(value)
    elif functionVariant == 3:
        return horner([1, 5, -4, -20], 4, value)
    elif functionVariant == 4:
        return math.sin(value)
    elif functionVariant == 5:
        return math.sin(value) - (7 * value)
    elif functionVariant == 6:
        return math.sin(value) + horner([1, -1/2, 1/5, -1/2], 4, value)
    elif functionVariant == 7:
        return abs(2 * math.cos(2 * value) + 1)
    elif functionVariant == 8:
        return 1 / horner([25, 0, 1], 3, value)
    else:
        print("Wrong function argument!!!")

def horner(tab, n, x):
    result = tab[0]
    for i in range(1, n):
        result = result * x + tab[i]
    return result

def czebyszew_nodes(a, b, n):
    k = np.arange(1, n+1)
    nodes = 0.5*(a+b) + 0.5*(b-a)*np.cos((2*k-1)*np.pi/(2*n))
    return nodes

def newton_interpolation(x, y):
    n = len(x) - 1
    c = y.copy()
    for j in range(1, n+1):
        for i in range(j, n+1):
            c[i] = (c[i] - c[j-1])/(x[i] - x[j-1])
    return c

def plot_interpolation(functionVariant, a, b, n, interpolationType='equidistant'):
    if interpolationType == 'equidistant':
        x = np.arange(a, b+(b-a)/1000, (b-a)/1000)
        nodes = np.linspace(a, b, num=n)
    elif interpolationType == 'chebyshev':
        x = np.linspace(a, b, num=1000)
        nodes = czebyszew_nodes(a, b, n)
    else:
        raise ValueError("Invalid interpolation type specified.")
    y = [calculateValueOfFunction(functionVariant, i) for i in nodes]
    yi = calculate_interpolated_values(y, x, nodes)
    plt.plot(x, yi, label='Interpolated function')
    if functionVariant.__class__ == "numpy.ndarray":
        plt.plot(x, functionVariant, label='Original function')
    else:
        plt.plot(x, [calculateValueOfFunction(functionVariant, i) for i in x], label='Original function')
    plt.plot(nodes, y, 'o', label='Interpolation nodes')
    plt.legend()
    plt.show()

selectedFunction = UI.printChooseFunctionMenu()
a, b = UI.printChooseRangeMenu()
nodesSelection = UI.printChooseNodesSelection()
numberOfNodes = UI.printChooseNumberOfNodes()
plot_interpolation(selectedFunction, a, b, numberOfNodes, nodesSelection)