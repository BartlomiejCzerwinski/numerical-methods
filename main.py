import matplotlib.pyplot as plt;
import math
import numpy as np

def printChooseVariantMenu():
    print("----------------------------------------")
    print("CHOOSE VARIANT")
    print("----------------------------------------")
    print("1. Bisection method")
    print("2. Regula falsi")
    selectedVariant = getInputFromUser("Variant")

def printChooseFunctionMenu():
    print("----------------------------------------")
    print("CHOOSE FUNCTION")
    print("----------------------------------------")
    print("1. 21x^3 + 32x^2 + 10x + 2")
    print("2. sin(x) - 1/2")
    print("3. 2^x")
    print("4. cos(20x) + x^3 - 1")
    print("5. 2^3x - 5x^3 - 5")
    selectedFunction = int(getInputFromUser("Function"))

def printChooseRangeMenu():
    print("----------------------------------------")
    print("CHOOSE RANGE")
    print("----------------------------------------")
    a = float(getInputFromUser("A"))
    b = float(getInputFromUser("B"))

def printChooseStopCondition():
    print("----------------------------------------")
    print("CHOOSE STOP CONDITION")
    print("----------------------------------------")
    print("1. Precision of results")
    print("2. Number of iterations")
    selectedStopCondition = int(getInputFromUser("Condition"))
def getInputFromUser(message):
    return input(message + ": ")

def calculateValueOfFunction(functionVariant, value):
    if functionVariant == 1:
        return (21 * (value ** 3)) + (32 * (value**2)) + (10 * value) +2
    elif functionVariant == 2:
        return math.sin(value) - 1/2
    elif functionVariant == 3:
        return 2 ** value
    elif functionVariant == 4:
        return math.cos(20 * value) + (value ** 3) + 2
    elif functionVariant == 5:
        return (2 ** (3 * value)) - (5 * (value ** 3)) - 5
    else :
        print("wrong function argument!!!")

def bisectionAlgorithm(a, b, stopValue):
    i = 0
    while not isIterationsReached(i, stopValue):
        midpoint = 0
        i += 1
        midpoint = (a + b) / 2

        if i == stopValue :
            print(midpoint)

        if calculateValueOfFunction(1, a) * calculateValueOfFunction(1, midpoint) < 0:
            b = midpoint
        elif calculateValueOfFunction(1, midpoint) * calculateValueOfFunction(1, b) < 0:
            a = midpoint

def isIterationsReached(i, stopValue):
    if i < stopValue:
        return False
    return True
def isEpsilonReached(e, eStop):
    if e < eStop:
        return True
    return False


bisectionAlgorithm(-10, 10, 20)






