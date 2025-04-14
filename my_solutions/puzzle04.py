#Programming for the Puzzled -- Srini Devadas
#Please Do Break the Crystal
#This is an interactive procedure that given n floors and d balls determines
#what floors to drop the balls from to minimize the worst-case number of
#drops required to determine the hardness coefficient of the crystal.
#The hardness coefficient will range from 0 (breaks at Floor 1) or n (does not
#break at n.
def howHardIsTheCrystal(n, d, inputs=[]):

    # Exercise 1
    # First determine the radix r
    r, d = determineRadixAndNumBalls(n, d)

    numBreaks, numDrops, prevFloor = 0, 0, 0
    low, high = 1, n
    floorNoBreak = [0] * d
    intervals = []
    for i in range(d):
        #Begin phase i
        for j in range(r-1):
            #increment ith digit of representation
            floorNoBreak[i] += 1
            Floor = convertToDecimal(r, d, floorNoBreak)
            #Make sure you aren't higher than the highest floor
            if Floor > n:
                floorNoBreak[i] -= 1
                break
            # Exercise 3
            print('Interval under consideration: [', low, ',', high, ']')
            intervals.append([low, high])
            print ('Drop ball', i+1, 'from Floor', Floor)
            yes = (inputs and numDrops < len(inputs) and inputs[numDrops])
            if not yes:
                yes = input('Did the ball break (yes/no)?:')
            numDrops += 1
            if yes == 'yes':
                numBreaks += 1
                floorNoBreak[i] -= 1
                high = Floor - 1
                break
            else:
                low = Floor + 1


    hardness = convertToDecimal(r, d, floorNoBreak)
    print('Hardness coefficient is', hardness)
    print('Total number of drops is', numDrops)
    # Exercise 2
    print('Total number of breaks is', numBreaks)

    return numBreaks, intervals

def convertToDecimal(r, d, rep):
    number = 0
    for i in range(d-1):
        number = (number + rep[i]) * r
    number += rep[d-1]

    return number

def determineRadixAndNumBalls(n, d):
    r = 1
    while (r**d <= n):
        r += 1
    # Maybe we can reduce the number of balls
    while (r**(d-1) > n):
        d -= 1
    
    print('Radix chosen is', r)
    print('Number of balls is', d)
    return r, d
