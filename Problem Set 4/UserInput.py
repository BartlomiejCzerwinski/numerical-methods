def printChooseFunctionMenu():
    print("----------------------------------------")
    print("CHOOSE FUNCTION")
    print("----------------------------------------")
    print("1. x^2 + 3")
    print("2. x^3 + 5x^2 - 4x - 20")
    print("3. cos(2x)")
    print("4. 2cos(2x) - 1")
    return int(input("Function: "))

def printChooseRangeMenu():
    print("----------------------------------------")
    print("CHOOSE RANGE")
    print("----------------------------------------")
    a = float(input("A: "))
    b = float(input("B: "))
    return a, b

def printChooseRangeVariantMenu():
    print("----------------------------------------")
    print("CHOOSE RANGE VARIANT")
    print("----------------------------------------")
    print("1. (-∞ ; +∞)")
    print("2. [a ; b]")
    return int(input("Variant: "))

def printChoosePrecisionMenu():
    print("----------------------------------------")
    print("ENTER PRECISION")
    print("----------------------------------------")
    return float(input("Precision: "))

def printChooseEnterNumberOfNodesMenu():
    print("----------------------------------------")
    print("ENTER NUMBER OF NODES")
    print("----------------------------------------")
    return int(input("Number of nodes: "))