#Programming for the Puzzled -- Srini Devadas
#Keep Those Queens Apart
#Given a 8 x 8 chess board, figure out how to place 8 Queens such that
#no Queen attacks another queen.
#This code uses a single-dimensional list to represent Queen positions


#This procedure checks that the most recently placed queen on the board on column
#current does not conflict with existing queens.
def noConflicts(board, current):
    for i in range(current):
        if (board[i] == board[current]):
            return False
        #We have two diagonals hence need the abs()
        if (current - i == abs(board[current] - board[i])):
            return False
    return True 


#This procedure places 8 Queens on a board so they don't conflict.
#It assumes n = 8 and won't work with other n!
def EightQueens(numSolutions, location, n=8):
    board = [-1] * n
    solutions = []
    for i in range(n):
        board[0] = i
        # Exercise 2
        if location[0] >= 0 and i != location[0]:
            continue
        for j in range(n):
            board[1] = j
            if (location[1] >= 0 and j != location[1]) or not noConflicts(board, 1):
                continue
            for k in range(n):
                board[2] = k
                if (location[2] >= 0 and k != location[2]) or not noConflicts(board, 2):
                    continue
                for l in range(n):
                    board[3] = l
                    if (location[3] >= 0 and l != location[3]) or not noConflicts(board, 3):
                        continue
                    for m in range(n):
                        board[4] = m
                        if (location[4] >= 0 and m != location[4]) or not noConflicts(board, 4):
                            continue
                        for o in range(n):
                            board[5] = o
                            if (location[5] >= 0 and n != location[5]) or not noConflicts(board, 5):
                                continue
                            for p in range(n):
                                board[6] = p
                                if (location[6] >= 0 and p != location[6]) or not noConflicts(board, 6):
                                    continue
                                for q in range(n):
                                    board[7] = q
                                    if location[7] >= 0 and q != location[7]:
                                        continue
                                    if noConflicts(board, 7):
                                        print (board)
                                        # Exercise 1
                                        solutions.append(board.copy())
                                        if len(solutions) == numSolutions:
                                            return solutions
    return solutions
