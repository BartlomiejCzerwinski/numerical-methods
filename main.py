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

printChooseVariantMenu()
printChooseFunctionMenu()
printChooseRangeMenu()
printChooseStopCondition()


