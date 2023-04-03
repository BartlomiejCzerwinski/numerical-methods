import numpy as np

def loadNumbersFromFile(file_path):
    matrix = []
    with open(file_path, 'r') as f:
        for line in f:
            row = [float(x) for x in line.split()]
            matrix.append(row)
    return np.array(matrix)

def createMatrix(dataMatrix):
    result = []
    for i in dataMatrix:
        result.append(i[0:-1])
    return np.array(result)

def createVector(dataMatrix):
    result = []
    for i in dataMatrix:
        result.append(i[len(i)-1])
    return np.array(result)

def divideRow(matrix, vector, rowNumber):
    pivot = matrix[rowNumber][rowNumber]
    for i in range(matrixSize):
        matrix[rowNumber][i] /= pivot
    vector[rowNumber] /= pivot
    return matrix, vector

def eliminateRow(matrix, vector,  rowNumber):
    matrixCopy = np.copy(matrix)
    for i in range(matrixSize):
        for j in range(matrixSize):
            if i != rowNumber:
                matrix[i][j] = matrix[i][j] - (matrixCopy[i][rowNumber] * matrix[rowNumber][j])
        if i != rowNumber:
            vector[i] = vector[i] - (matrixCopy[i][rowNumber] * vector[rowNumber])
    return matrix, vector

def swapRowsIfDiagonalZero(matrix, vector, startPosition):
    n = len(matrix)
    for i in range(startPosition, n):
        if matrix[i][i] == 0:
            for j in range(i+1, n):
                if matrix[j][i] != 0:
                    tmp = np.copy(matrix[i])
                    matrix[i] = matrix[j]
                    matrix[j] = tmp
                    tmp2 = vector[i]
                    vector[i] = vector[j]
                    vector[j] = tmp2
                    return matrix, vector
    return matrix, vector

def isMatrixIndeterminate(matrix, vector):
    for i in range(matrixSize):
        if round(sum(matrix[i]), 10) == 0 and round(vector[i], 10) == 0:
            return True
    return False

def isMatrixInconsistent(matrix, vector):
    for i in range(matrixSize):
        if round(sum(matrix[i]), 10) == 0 and round(vector[i], 10) != 0:
            return True
    return False

def printResults(vector):
    for i in range(len(vector)):
        print("x" + str(i) + " = " + str(round(vector[i], 10)))

def gaussJordanAlgorithm(matrix, vector):
    for i in range(matrixSize):
        if isMatrixIndeterminate(matrix, vector):
            print("NIEOZNACZONY")
            return
        if isMatrixInconsistent(matrix, vector):
            print("SPRZECZNY")
            return
        matrix, vector = swapRowsIfDiagonalZero(matrix, vector, i)
        matrix, vector = divideRow(matrix, vector, i)
        matrix, vector = eliminateRow(matrix, vector, i)
    printResults(vector)

data = loadNumbersFromFile("data.txt")
matrix = createMatrix(data)
vector = createVector(data)
matrixSize = len(vector)
gaussJordanAlgorithm(matrix, vector)