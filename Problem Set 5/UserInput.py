def printChooseFunctionMenu():
    print("----------------------------------------")
    print("CHOOSE FUNCTION")
    print("----------------------------------------")
    print("1. 3x + 5")
    print("2. |X|")
    print("3. 2x^2 + x - 2")
    print("4. sin(x)")
    print("5. cos(2x + 1)")
    return int(input("Function: "))

def printChooseRangeMenu():
    print("----------------------------------------")
    print("CHOOSE RANGE")
    print("----------------------------------------")
    a = float(input("A: "))
    b = float(input("B: "))
    return a, b

def printChooseEnterNumberOfNodesMenu():
    print("----------------------------------------")
    print("ENTER NUMBER OF NODES")
    print("----------------------------------------")
    return int(input("Number of nodes: "))

def printChooseEnterPolynomialDegree():
    print("----------------------------------------")
    print("ENTER POLYNOMIAL DEGREE")
    print("----------------------------------------")
    return int(input("Degree: "))