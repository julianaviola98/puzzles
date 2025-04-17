#Programming for the Puzzled -- Srini Devadas
#You Will Never Want to Play Sudoku Again
#Given a partially filled in Sudoku board, complete the puzzle
#obeying the rules of Sudoku

backtracks = 0
NORMAL_EMPTY_SQUARE = 0
EVEN_EMPTY_SQUARE = -2

#x varies from entry1 to entry2 - 1, y varies from entry3 to entry4 - 1 
sectors = [ [0, 3, 0, 3], [3, 6, 0, 3], [6, 9, 0, 3],
            [0, 3, 3, 6], [3, 6, 3, 6], [6, 9, 3, 6],
            [0, 3, 6, 9], [3, 6, 6, 9], [6, 9, 6, 9] ]

#This procedure finds the next empty square to fill on the Sudoku grid
def findNextCellToFill(grid, solveEven):
    #Look for an unfilled grid location
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == NORMAL_EMPTY_SQUARE or (solveEven and grid[x][y] == EVEN_EMPTY_SQUARE):
                return x,y
    return -1,-1

#This procedure checks if setting the (i, j) square to e is valid
def isValid(grid, i, j, e, solveDiagonal, solveEven):
    if solveEven and grid[i][j] == EVEN_EMPTY_SQUARE and e % 2 == 1:
        return False
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            #finding the top left x,y co-ordinates of
            #the section or sub-grid containing the i,j cell
            secTopX, secTopY = 3 *(i//3), 3 *(j//3)
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if grid[x][y] == e:
                        return False
            # Check the diagonals
            # Case 1: Top left to bottom right
            if solveDiagonal and i == j and any([e == grid[x][x] for x in range(9)]):
                return False
            # Case 2: Bottom left to top right
            if solveDiagonal and i + j == 8 and any([e == grid[x][8 - x] for x in range(9)]):
                return False
            return True
    return False


#This procedure makes implications based on existing numbers on squares
def makeImplications(grid, i, j, e, solveDiagonal, solveEven):

    global sectors

    prevValue = grid[i][j]
    grid[i][j] = e
    impl = [(i, j, e, prevValue)]
    addedNewImpl = True

    # Exercise 1
    while addedNewImpl:
        addedNewImpl = False
        for k in range(len(sectors)):

            sectinfo = []

            #find missing elements in ith sector
            vset = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            for x in range(sectors[k][0], sectors[k][1]):
                for y in range(sectors[k][2], sectors[k][3]):
                        if solveEven:
                            if grid[x][y] != NORMAL_EMPTY_SQUARE and grid[x][y] != EVEN_EMPTY_SQUARE:
                                vset.remove(grid[x][y])
                        else:
                            if grid[x][y] != NORMAL_EMPTY_SQUARE:
                                vset.remove(grid[x][y])

            #attach copy of vset to each missing square in ith sector
            for x in range(sectors[k][0], sectors[k][1]):
                for y in range(sectors[k][2], sectors[k][3]):
                    if solveEven:
                        if grid[x][y] == NORMAL_EMPTY_SQUARE or grid[x][y] == EVEN_EMPTY_SQUARE:
                            sectinfo.append([x, y, vset.copy()])
                    else:
                        if grid[x][y] == NORMAL_EMPTY_SQUARE:
                            sectinfo.append([x, y, vset.copy()])
            
            for m in range(len(sectinfo)):
                sin = sectinfo[m]
                
                #find the set of elements on the row corresponding to m and remove them
                rowv = set()
                for y in range(9):
                    rowv.add(grid[sin[0]][y])
                left = sin[2].difference(rowv)
                
                #find the set of elements on the column corresponding to m and remove them
                colv = set()
                for x in range(9):
                    colv.add(grid[x][sin[1]])
                left = left.difference(colv)
                            
                #check if the vset is a singleton
                if len(left) == 1:
                    val = left.pop()
                    if isValid(grid, sin[0], sin[1], val, solveDiagonal, solveEven):
                        prevValue = grid[sin[0]][sin[1]]
                        grid[sin[0]][sin[1]] = val
                        impl.append((sin[0], sin[1], val, prevValue))
                        addedNewImpl = True
    return impl

#This procedure undoes all the implications
def undoImplications(grid, impl):
    for i in range(len(impl)):
        grid[impl[i][0]][impl[i][1]] = impl[i][3]
    return


#This procedure fills in the missing squares of a Sudoku puzzle
#obeying the Sudoku rules by guessing when it has to and performing
#implications when it can
def solveSudokuOpt(grid, i = 0, j = 0, solveDiagonal = False, solveEven = False):

    global backtracks

    #find the next empty cell to fill
    i, j = findNextCellToFill(grid, solveEven)
    if i == -1:
        return True

    for e in range(1, 10):
        #Try different values in i, j location
        if isValid(grid, i, j, e, solveDiagonal, solveEven):

            impl = makeImplications(grid, i, j, e, solveDiagonal, solveEven)
            
            if solveSudokuOpt(grid, i, j, solveDiagonal, solveEven):
                return grid, backtracks
            #Undo the current cell for backtracking
            backtracks += 1
            undoImplications(grid, impl)

    return False

def printSudoku(grid):
    numrow = 0
    for row in grid:
        if numrow % 3 == 0 and numrow != 0:
            print (' ')
        print (row[0:3], ' ', row[3:6], ' ', row[6:9])
        numrow += 1       
    return
