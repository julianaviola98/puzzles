#Programming for the Puzzled -- Srini Devadas
#The Best Time to Party
#Given a list of intervals when celebrities will be at the party
#Output is the time that you want to go the party when the maximum number of
#celebrities are still there.
#Clever algorithm that will work with fractional times

sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12),
            (9, 10), (10, 11), (10, 12), (11, 12)]
sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0),
          (8.0, 10.0), (9.0, 12.0), (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]
sched3 = [(6, 7), (7,9), (10, 11), (10, 12), (8, 10), (9, 11), (6, 8),
          (9, 10), (11, 12), (11, 13), (11, 14)]
sched4 = [(6.0, 8.0, 2), (6.5, 12.0, 1), (6.5, 7.0, 2),
          (7.0, 8.0, 2), (7.5, 10.0, 3), (8.0, 9.0, 2),
          (8.0, 10.0, 1), (9.0, 12.0, 2), (9.5, 10.0, 4),
          (10.0, 11.0, 2), (10.0, 12.0, 3), (11.0, 12.0, 7)]

# Exercise 1: Add ystart and yend
def bestTimeToPartySmart(schedule, ystart, yend):
    #Convert schedule to list of start times and end times marked as such
    times = []
    for c in schedule:
        times.append((c[0], 'start'))
        times.append((c[1], 'end'))

    #Sort the list of times.
    #Each time is a start or end time of a celebrity sighting.
    sortlist(times)
##    print times

    maxcount, time = chooseTime(times, ystart, yend)


    #Output best time to party
    print ('Best time to attend the party is at', time,\
           'o\'clock', ':', maxcount, 'celebrities will be attending!')
    

#Sort the elements of tlist in ascending order
#Sorting is based on the value of the element tuple (both items!)
#The original code had a bug in that it did not look at the second
#item of each tuple and ensure that (x, 'end') of one interval
#is sorted before (x, 'start') of a different tuple.
def sortlist(tlist):
    for index in range(len(tlist)-1):
        ismall = index
        for i in range(index, len(tlist)):
            #Sort based on first item of tuple
            if tlist[ismall][0] > tlist[i][0] or \
               (tlist[ismall][0] == tlist[i][0] and \
                tlist[ismall][1] > tlist[i][1]):
                ismall = i
        #Swap the positions of the elements at index and ismall indices
        tlist[index], tlist[ismall] = tlist[ismall], tlist[index]
    
    return


def chooseTime(times, ystart, yend):
    
    rcount = 0
    maxcount = 0
    time = 0
    
    #Range through the times computing a running count of celebrities
    for t in times:
        if ystart <= t[0] and t[0] < yend:
            if t[1] == 'start':
                rcount = rcount + 1
            elif t[1] == 'end':
                rcount = rcount - 1
            if rcount > maxcount:
                maxcount = rcount
                time = t[0]
            
    return maxcount, time

# Exercise 2
def weightedChooseTime(times):
    count = 0
    maxCount = 0
    time = 0
    
    #Range through the times computing a running count of celebrities
    for t in times:
        if t[1] == 'start':
            count += t[2]
        elif t[1] == 'end':
            count -= t[2]
        if count > maxCount:
            maxCount = count
            time = t[0]
            
    return maxCount, time

# Exercise 3
def alternativeBestTimeToPartySmart(schedule):
    maxCount = 0
    bestTime = 0
    for x in schedule:
        startTime = x[0]
        count = 0
        for y in schedule:
            if startTime >= y[0] and startTime < y[1]:
                count += 1
        if count > maxCount:
            maxCount = count
            bestTime = startTime
    print ('Best time to attend the party is at', bestTime,\
           'o\'clock', ':', maxCount, 'celebrities will be attending!')
    
def weightedBestTimeToPartySmart(schedule):
    times = []
    for c in schedule:
        times.append((c[0], 'start', c[2]))
        times.append((c[1], 'end', c[2]))

    sortlist(times)

    maxCount, time = weightedChooseTime(times)

    print ('Best time to attend the party is at', time,\
           'o\'clock', ':', maxCount, 'celebrities will be attending!')


bestTimeToPartySmart(sched, 6, 12)
bestTimeToPartySmart(sched2, 6, 12)
bestTimeToPartySmart(sched3, 6, 14)
alternativeBestTimeToPartySmart(sched)
alternativeBestTimeToPartySmart(sched2)
alternativeBestTimeToPartySmart(sched3)
weightedBestTimeToPartySmart(sched4)