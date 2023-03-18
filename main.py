import matplotlib.pyplot as plt;
import math
import numpy as np

selectedVariant = 0
selectedFunction = 0
selectedA = 0
selectedB = 0
selectedNumberOfIterations = 0;
selectedStopValue = 0

def printChooseVariantMenu():
    print("----------------------------------------")
    print("CHOOSE VARIANT")
    print("----------------------------------------")
    print("1. Bisection method")
    print("2. Regula falsi")
    return int(getInputFromUser("Variant"))

def printChooseFunctionMenu():
    print("----------------------------------------")
    print("CHOOSE FUNCTION")
    print("----------------------------------------")
    print("1. x^3 - 1/2x^2 + 1/5x - 1/2")
    print("2. sin(x)")
    print("3. 2^x - 3")
    print("4. cos(x) + x^3 - 1")
    print("5. 2^3x - 5x^3 - 5")
    return int(getInputFromUser("Function"))

def printChooseRangeMenu():
    print("----------------------------------------")
    print("CHOOSE RANGE")
    print("----------------------------------------")
    a = float(getInputFromUser("A"))
    b = float(getInputFromUser("B"))
    return a, b

def printSetEpsilon():
    print("----------------------------------------")
    print("SET EPSILON")
    print("----------------------------------------")
    return float(getInputFromUser("Epsilon"))

def printSetNumberOfIterations():
    print("----------------------------------------")
    print("SET NUMBER OF ITERATIONS")
    print("----------------------------------------")
    return float(getInputFromUser("Number of iterations"))

def printChooseStopCondition():
    print("----------------------------------------")
    print("CHOOSE STOP CONDITION")
    print("----------------------------------------")
    print("1. Precision of results")
    print("2. Number of iterations")
    return int(getInputFromUser("Condition"))

def getInputFromUser(message):
    return input(message + ": ")

def calculateValueOfFunction(functionVariant, value):
    if functionVariant == 1:
        return (value ** 3) - ((1/2) * (value**2)) + ((1/5) * value) - (1/2)
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

def bisectionAlgorithm(functionNumber, a, b):
    midpoint = (a + b) / 2

    if calculateValueOfFunction(functionNumber, a) * calculateValueOfFunction(functionNumber, midpoint) < 0:
        b = midpoint
    elif calculateValueOfFunction(functionNumber, midpoint) * calculateValueOfFunction(functionNumber, b) < 0:
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

def bisectionAlgorithmController(stopCondition, functionNumber, a, b, stopValue):
    actualNumberOfIterations = 0;
    plotA = a
    plotB = b
    if stopCondition == 1:
        a, b, xi = bisectionAlgorithm(functionNumber, a, b)
        actualNumberOfIterations += 1
        while not isEpsilonReached(calculateValueOfFunction(functionNumber, xi), stopValue):
            actualNumberOfIterations += 1
            a, b, xi = bisectionAlgorithm(functionNumber, a, b)
        print("Zero: ", xi)
        print("Iterations number: ", actualNumberOfIterations)
        drawPlot(functionNumber, plotA, plotB, xi)

    elif stopCondition == 2:
        while not isIterationsReached(actualNumberOfIterations, stopValue):
            actualNumberOfIterations += 1
            print(actualNumberOfIterations)
            a, b, xi =  bisectionAlgorithm(functionNumber, a, b)
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


selectedVariant = printChooseVariantMenu()
selectedFunction = printChooseFunctionMenu()
selectedA, selectedB = printChooseRangeMenu()
selectedStopCondition = printChooseStopCondition()
if selectedStopCondition == 1:
    selectedStopValue = printSetEpsilon()
elif selectedStopCondition == 2:
    selectedStopValue = printSetNumberOfIterations()

bisectionAlgorithmController(selectedStopCondition, selectedFunction, selectedA, selectedB, selectedStopValue)

