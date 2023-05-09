def printChooseFunctionMenu():
    print("----------------------------------------")
    print("CHOOSE FUNCTION")
    print("----------------------------------------")
    print("1. 5x - 2")
    print("2. |x|")
    print("3. x^3 + 5x^2 - 4x -20")
    print("4. sin(x)")
    print("5. sin(x) - 7x")
    print("6. sin(x) + x^3 - 1/2x^2 + 1/5x - 1/2")
    print("7. |2cos(2x) + 1|")
    print("8. 1 / (1 + 25x^2)")
    return int(input("Function: "))

def printChooseRangeMenu():
    print("----------------------------------------")
    print("CHOOSE RANGE")
    print("----------------------------------------")
    a = float(input("A: "))
    b = float(input("B: "))
    return a, b

def printChooseNodesSelection():
    print("----------------------------------------")
    print("CHOOSE NODES SELECTION")
    print("----------------------------------------")
    print("1. Equidistant")
    print("2. Chebyshev")
    variant = int(input("Variant: "))
    if variant == 1:
        return "equidistant"
    if variant == 2:
        return "chebyshev"

def printChooseNumberOfNodes():
    print("----------------------------------------")
    print("SELECT NUMBER OF NODES")
    print("----------------------------------------")
    num = int(input("Number of nodes: "))
    return num