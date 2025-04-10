#Programming for the Puzzled -- Srini Devadas
#You Will All Conform
#Input is a vector of F's and B's, in terms of forwards and backwards caps
#Output is a set of commands (printed out) to get either all F's or all B's
#Fewest commands are the goal

caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F' ]
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F' ]
# Exercise 3
cap3 = ['F', 'F', 'B', 'H', 'B', 'F', 'B', 'B', 'B', 'F', 'H', 'F', 'F']

def pleaseConformOpt(caps):
    #Initialization
    start = 0
    forward = 0
    backward = 0
    intervals = []

    caps = caps + ['END']

    #Determine intervals where caps are on in the same direction
    for i in range(1, len(caps)):
        if caps[start] != caps[i]:
            # each interval is a tuple with 3 elements (start, end, type)
            intervals.append((start, i - 1, caps[start]))
            
            if caps[start] == 'F':
                forward += 1
            elif caps[start] == 'B':
                backward += 1
            start = i

    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2] == flip:
            # Exercise 1
            if t[0] == t[1]:
                print('Person at position', t[0], 'flip your cap!')
            else:
                print ('People in positions', t[0], 'through', t[1], 'flip your caps!')


def pleaseConformOnepass(caps):
    caps = [] if not caps else caps + [caps[0]]
    for i in range(1, len(caps)):
        if caps[i] != caps[i-1]:
            if caps[i] != caps[0]:
                # Exercise 2
                if i+1 < len(caps) and caps[i] != caps[i+1]:
                    print('Person in position', i, 'flip your cap!')
                else:
                    print('People in positions', i, end='')
            else:
                if i-1 >= 0 and i-2 >= 0 and caps[i-1] == caps[i-2]:
                    print(' through', i-1, 'flip your caps!')

                           
pleaseConformOpt(caps)
pleaseConformOnepass(caps)
pleaseConformOpt(cap2)
pleaseConformOnepass(cap2)
pleaseConformOpt(cap3)
# pleaseConformOnepass hasn't been updated to handle hatless people
pleaseConformOpt([])
pleaseConformOnepass([])
