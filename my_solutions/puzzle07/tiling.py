#Programming for the Puzzled -- Srini Devadas
#Tile that Courtyard, Please
#Given n in a 2^n x 2^n checkyard with a missing square at position (r, c), 
#find tiling of yard with trominoes (L-shaped dominoes).
#This version works directly on the given grid, and does NOT make copies
#of the grid for recursive calls.

import itertools

EMPTYPIECE = -1



#This procedure is the main engine of recursive algorithm
#nextPiece is the number of next available tromino piece
#The origin coordinates of the yard are given by originR and originC
def recursiveTile(yard, size, originR, originC, rMiss, cMiss, nextPiece):

    #quadrant of missing square: 0 (upper left), 1 (upper right),
    #                            2 (lower left), 3 (lower right)
    quadMiss = 2*(rMiss >= size//2) + (cMiss >= size//2)
    
    #base case of 2x2 yard
    if size == 2: 
        piecePos = [(0,0), (0,1), (1,0), (1,1)]
        piecePos.pop(quadMiss)
        for (r, c) in piecePos:
            yard[originR + r][originC + c] = nextPiece
        nextPiece = nextPiece + 1
        return nextPiece

    #recurse on each quadrant
    
    for quad in range(4):
        #Each quadrant has a different origin
        #Quadrant 0 has origin (0, 0), Quadrant 1 has origin (0, size//2)
        #Quadrant 2 has origin (size//2, 0), Quadrant 3 has origin (size//2, size//2)
        shiftR = size//2 * (quad >= 2)
        shiftC = size//2 * (quad % 2 == 1)
        if quad == quadMiss:
            #Pass the new origin and the shifted rMiss and cMiss
            nextPiece = recursiveTile(yard, size//2, originR + shiftR,\
                originC + shiftC, rMiss - shiftR, cMiss - shiftC, nextPiece)

        else:
            #The missing square is different for each of the other 3 quadrants
            newrMiss = (size//2 - 1) * (quad < 2)
            newcMiss = (size//2 - 1) * (quad % 2 == 0)
            nextPiece = recursiveTile(yard, size//2, originR + shiftR,\
                            originC + shiftC, newrMiss, newcMiss, nextPiece)


    #place center tromino
    centerPos = [(r + size//2 - 1, c + size//2 - 1)
                 for (r,c) in [(0,0), (0,1), (1,0), (1,1)]]
    centerPos.pop(quadMiss)
    for (r,c) in centerPos: # assign tile to 3 center squares
        yard[originR + r][originC + c] = nextPiece
    nextPiece = nextPiece + 1

    return nextPiece

#This procedure is a wrapper for recursiveTile that does all the work
def tileMissingYard(n, rMiss, cMiss):
    #Initialize yard, this is the only memory that will be modified!
    yard = [[EMPTYPIECE for i in range(2**n)]
            for j in range(2**n)] 
    recursiveTile(yard, 2**n, 0, 0, rMiss, cMiss, 0)
    return yard

# Exercise 1
def tileYardWith4MissingTiles(n, missingTileLocations):
    # Case 1: The four missing tiles are in four different quadrants.
    # Number the quadrants like so:
    # 0 = top left
    # 1 = top right
    # 2 = bottom left
    # 3 = bottom right
    size = 2**n
    halfSize = size // 2
    quadrantCount = [0] * 4
    for missingTileLocation in missingTileLocations:
        row = missingTileLocation[0]
        column = missingTileLocation[1]
        if row < halfSize:
            if column < halfSize:
                quadrantCount[0] += 1
            else:
                quadrantCount[1] += 1
        else:
            if column < halfSize:
                quadrantCount[2] += 1
            else:
                quadrantCount[3] += 1
    if quadrantCount == [1, 1, 1, 1]:
        return True

    # Case 2: Any three of the four tiles are such that you can tile them using a tromino.
    for subset in itertools.combinations(missingTileLocations, 3):
        coordinateDiffs = []
        for pair in itertools.combinations(subset, 2):
            coordinateDiff = (pair[0][0] - pair[1][0], pair[0][1] - pair[1][1])
            coordinateDiffs.append(coordinateDiff)
        if ((0, 1) in coordinateDiffs or (0, -1) in coordinateDiffs) and ((1, 0) in coordinateDiffs or (-1, 0) in coordinateDiffs):
            return True
        
    return False

#This procedure prints a given tiled yard using letters for tiles
def printYard(yard):
    for i in range(len(yard)):
        row = ''
        for j in range(len(yard[0])):
            if yard[i][j] != EMPTYPIECE:
                row += chr((yard[i][j] % 26) + ord('A'))
            else:
                row += ' '
        print (row)


printYard(tileMissingYard(3, 4, 6))
printYard(tileMissingYard(4, 5, 7))
