def printChooseVariantMenu():
    print("----------------------------------------")
    print("CHOOSE VARIANT")
    print("----------------------------------------")
    print("1. Bisection method")
    print("2. Regula falsi")
    return int(input("Variant: "))

def printChooseFunctionMenu():
    print("----------------------------------------")
    print("CHOOSE FUNCTION")
    print("----------------------------------------")
    print("1. x^3 - 1/2x^2 + 1/5x - 1/2")
    print("2. sin(x)")
    print("3. 2^x - 3")
    print("4. cos(x) + x^3 - 1")
    print("5. 2^3x - 5x^3 - 5")
    return int(input("Function: "))

def printChooseRangeMenu():
    print("----------------------------------------")
    print("CHOOSE RANGE")
    print("----------------------------------------")
    a = float(input("A: "))
    b = float(input("B: "))
    return a, b

def printSetEpsilon():
    print("----------------------------------------")
    print("SET EPSILON")
    print("----------------------------------------")
    return float(input("Epsilon: "))

def printSetNumberOfIterations():
    print("----------------------------------------")
    print("SET NUMBER OF ITERATIONS")
    print("----------------------------------------")
    return float(input("Number of iterations: "))

def printChooseStopCondition():
    print("----------------------------------------")
    print("CHOOSE STOP CONDITION")
    print("----------------------------------------")
    print("1. Precision of results")
    print("2. Number of iterations")
    return int(input("Condition: "))