import matplotlib.pyplot as plt;
import math
import numpy as np
import userInput as uI

selectedVariant = 0
selectedFunction = 0
selectedA = 0
selectedB = 0
selectedNumberOfIterations = 0
selectedStopValue = 0

def calculateValueOfFunction(functionVariant, value):
    if functionVariant == 1:
        return horner([1, -1/2, 1/5, -1/2], 4, value)
    elif functionVariant == 2:
        return math.sin(value)
    elif functionVariant == 3:
        return (2 ** value) -3
    elif functionVariant == 4:
        return math.cos(value) + (value ** 3) - 1
    elif functionVariant == 5:
        return (2 ** (3 * value)) - (5 * (value ** 3)) - 5
    else :
        print("wrong function argument!!!")

def horner(tab, n, x):
    result = tab[0]
    for i in range(1, n):
        result = result * x + tab[i]
    return result

def bisectionAlgorithm(functionNumber, a, b):
    midpoint = (a + b) / 2

    if calculateValueOfFunction(functionNumber, a) * calculateValueOfFunction(functionNumber, midpoint) < 0:
        b = midpoint
    elif calculateValueOfFunction(functionNumber, midpoint) * calculateValueOfFunction(functionNumber, b) < 0:
        a = midpoint

    return a, b, midpoint

def regulaFalsiAlgorithm(functionNumber, a, b):
    midpoint = ((a * calculateValueOfFunction(functionNumber, b)) - (
                b * calculateValueOfFunction(functionNumber, a))) / (
                calculateValueOfFunction(functionNumber, b) - calculateValueOfFunction(functionNumber,a))

    if calculateValueOfFunction(functionNumber, midpoint) * calculateValueOfFunction(functionNumber, a) < 0:
        b = midpoint
    else:
        a = midpoint
    return a, b, midpoint

def drawPlot(functionNumber, a, b, root):
    x = np.linspace(a, b, 1000)
    y = [calculateValueOfFunction(functionNumber, xi) for xi in x]

    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.grid(True)

    ax.set_xlabel('x')
    ax.set_ylabel('y')

    title = f'Function Plot (Function number {functionNumber})'
    ax.set_title(title)

    ax.plot(root, 0, marker='o', markersize=8, color="red")

    ax.set_xlim([a, b])
    ax.set_ylim([min(y)-0.1, max(y)+0.1])

    plt.show()

def setUsingAlgorithm():
    if selectedVariant == 1:
        return bisectionAlgorithm
    else:
        return regulaFalsiAlgorithm

def algorithmController(stopCondition, functionNumber, a, b, stopValue):
    if calculateValueOfFunction(functionNumber, a) * calculateValueOfFunction(functionNumber, b) > 0:
        print("There is no zero points on given range")
        return

    algorithm = setUsingAlgorithm()
    actualNumberOfIterations = 0
    plotA = a
    plotB = b

    if stopCondition == 1:
        a, b, xi = algorithm(functionNumber, a, b)
        actualNumberOfIterations += 1
        while not isEpsilonReached(calculateValueOfFunction(functionNumber, xi), stopValue):
            actualNumberOfIterations += 1
            a, b, xi = algorithm(functionNumber, a, b)

    elif stopCondition == 2:
        while not isIterationsReached(actualNumberOfIterations, stopValue):
            actualNumberOfIterations += 1
            a, b, xi = algorithm(functionNumber, a, b)

    print("Zero: ", xi)
    print("Iterations number: ", actualNumberOfIterations)
    drawPlot(functionNumber, plotA, plotB, xi)

def isIterationsReached(i, stopValue):
    if i < stopValue:
        return False
    return True
def isEpsilonReached(e, eStop):
    if abs(e) < eStop:
        return True
    return False


selectedVariant = uI.printChooseVariantMenu()
selectedFunction = uI.printChooseFunctionMenu()
selectedA, selectedB = uI.printChooseRangeMenu()
selectedStopCondition = uI.printChooseStopCondition()
if selectedStopCondition == 1:
    selectedStopValue = uI.printSetEpsilon()
elif selectedStopCondition == 2:
    selectedStopValue = uI.printSetNumberOfIterations()

algorithmController(selectedStopCondition, selectedFunction, selectedA, selectedB, selectedStopValue)