def twoDimensionalBinarySearch(value, matrix):
    return twoDimensionalBinarySearchHelper(value, matrix, 0, 0)

def twoDimensionalBinarySearchHelper(value, matrix, rowOffset, columnOffset):
    height = len(matrix)
    width = len(matrix[0]) if len(matrix) > 0 else 0
    i, j = height // 2, width // 2
    if height == 0 or width == 0 or (height == 1 and width == 1 and matrix[0][0] != value):
        return (-1, -1)
    if matrix[i][j] == value:
        return (i + rowOffset, j + columnOffset)
    
    upperRightQuadrant = [matrix[i][width//2:] for i in range(height // 2)]
    bottomLeftQuadrant = [matrix[i][:width//2] for i in range(height // 2, height)]
    if matrix[i][j] < value:
        bottomRightQuadrant = [matrix[i][width//2:] for i in range(height // 2, height)]
        valueInUpperRight = twoDimensionalBinarySearchHelper(value, upperRightQuadrant, rowOffset, columnOffset + width // 2)
        valueInBottomLeft = twoDimensionalBinarySearchHelper(value, bottomLeftQuadrant, rowOffset + height // 2, columnOffset)
        valueInBottomRight = twoDimensionalBinarySearchHelper(value, bottomRightQuadrant, rowOffset + height // 2, columnOffset + width // 2)
        return foundValue(valueInUpperRight) or foundValue(valueInBottomLeft) or foundValue(valueInBottomRight) or (-1, -1)
    else:
        upperLeftQuadrant = [matrix[i][:width//2] for i in range(height // 2)]
        valueInUpperLeft = twoDimensionalBinarySearchHelper(value, upperLeftQuadrant, rowOffset, columnOffset)
        valueInUpperRight = twoDimensionalBinarySearchHelper(value, upperRightQuadrant, rowOffset, columnOffset + width // 2)
        valueInBottomLeft = twoDimensionalBinarySearchHelper(value, bottomLeftQuadrant, rowOffset + height // 2, columnOffset)
        return foundValue(valueInUpperLeft) or foundValue(valueInUpperRight) or foundValue(valueInBottomLeft) or (-1, -1)

def foundValue(coordinates):
    return coordinates if coordinates != (-1, -1) else False

def altAlgorithm(value, matrix):
    return altAlgorithmHelper(value, matrix, 0)

def altAlgorithmHelper(value, matrix, rowOffset):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return (-1, -1)
    topRight = matrix[0][len(matrix[0])-1]
    if topRight == value:
        return (0 + rowOffset, len(matrix[0])-1)
    elif topRight < value:
        newMatrix = [matrix[i] for i in range(1, len(matrix))]
        return altAlgorithmHelper(value, newMatrix, rowOffset+1)
    else:
        newMatrix = [matrix[i][:len(matrix[i])-1] for i in range(len(matrix))]
        return altAlgorithmHelper(value, newMatrix, rowOffset)