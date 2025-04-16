#Programming for the Puzzled -- Srini Devadas
#A Profusion of Queens
#Given the dimension of a square "chess" board, call it N, find a placement
#of N queens such that no two Queens attack each other using recursive search

#This procedure initializes the board to be empty, calls the recursive N-queens
#procedure and prints the returned solution
def nQueens(size, location):
    board = [-1] * size
    rQueens(board, 0, size, location)
    print(board)
    return printSolution(board)

# Exercise 1
def printSolution(board):
    size = len(board)
    output = ''
    for i in range(size):
        for j in range(size):
            end = ' '
            if j == size - 1:
                if i != size - 1:
                    end='\n'
                else:
                    end=''
            if board[j] == i:
                output += 'Q' + end
            else:
                output += '.' + end
    print(output)
    return output

#This procedure checks that the most recently placed queen on column current
#does not conflict with queens in columns to the left.
def noConflicts(board, current):
    for i in range(current):
        if (board[i] == board[current]):
            return False
        if (current - i == abs(board[current] - board[i])):
            return False
    return True 


#This procedure places a queens on the board on a given column so it does
#not conflict with the existing queens, and then calls itself recursively
#to place subsequent queens till the requisite number of queens are placed
def rQueens(board, current, size, location):
    if (current == size):
        return True
    else:
        for i in range(size):
            board[current] = i
            if location[current] != -1 and location[current] != i:
                continue
            if (noConflicts(board, current)):
                done = rQueens(board, current + 1, size, location)
                if (done):
                    return True
        return False
