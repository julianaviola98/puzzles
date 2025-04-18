#Programming for the Puzzled -- Srini Devadas
#The Disorganized Handyman
#A recursive sorting algorithm based on pivoting where a pivot is selected
#and the list split into three lists: the first containing elements smaller
#than the pivot, second elements equal to the pivot, and the third containing
#elements greater than the pivot. These sublists are recursively sorted.


#This procedure selects a pivot and partitions the list into 3 sublists
#It only uses one element worth of additional storage for the pivot!
def pivotPartitionClever(lst, start, end):
    pivot = lst[end] 
    bottom = start - 1       
    top = end
    moves = 0
    iterations = 0

    done = False
    while not done: 

        while not done:
            iterations += 1
            #Move rightward from left searching for element > pivot
            bottom += 1 
            if bottom == top: 
                done = True 
                break
            if lst[bottom] > pivot: 
                lst[top] = lst[bottom]
                moves += 1
                #print (lst, 'bottom =', bottom, 'top = ', top)
                break 

        while not done:
            iterations += 1
            #Move leftward from right searching for element < pivot
            top -= 1
            if top == bottom: 
                done = True 
                break
            if lst[top] < pivot: 
                lst[bottom] = lst[top]
                moves += 1
                #print (lst, 'bottom =', bottom, 'top = ', top)
                break 

    lst[top] = pivot 
    #print (lst)
    return top, moves, iterations


def quicksort(lst, start, end):
    moves = 0
    iterations = 0
    if start < end: 
        #print ('Partition start: bottom =', start - 1, 'top = ', end)
        #print (lst)
        split, moves, iterations = pivotPartitionClever(lst, start, end) 
        #print ('Partition end')
        _, newMoves, newIterations = quicksort(lst, start, split - 1)
        moves += newMoves
        iterations += newIterations
        _, newMoves, newIterations = quicksort(lst, split + 1, end)
        moves += newMoves
        iterations += newIterations
    return lst, moves, iterations

def quickselect(lst, start, end, k):
    if start < end:
        split, _, _ = pivotPartitionClever(lst, start, end)
        if split == k:
            return lst[split]
        elif split < k:
            return quickselect(lst, split + 1, end, k)
        else:
            return quickselect(lst, start, split - 1, k)
    return lst[k]
