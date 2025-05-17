from math import prod
invalid_squares = [1,9]
sequences = []

def backtracking(arr):
    if len(arr) == 11:
        sequences.append(arr)
        return
    
    backtracking(arr + [0])

    if len(arr) not in invalid_squares:
        if len(arr) >= 2:
            if arr[-1] != 1 and arr[-2] != 1:
                backtracking(arr + [1])
        elif len(arr) ==1:
            if arr[-1] != 1:
                backtracking(arr + [1])
        elif len(arr) == 0:
            backtracking(arr + [1])

def ones(array):
    res = []
    for arr in array:
        cur = []
        for i,num in enumerate(arr):
            
            if num==1:
                
                cur.append(i)
        res.append(cur)
    
    return res


backtracking([])

#print(sequences)
#print(ones(sequences))

total=[]
def combinations(arrays):

    for array in arrays:
        currarr = []
        currd = 0

        for num in array:
            if num ==1:
                if currd>1:
                    currarr.append(currd)
                    currd =0
            elif num == 0:
                currd +=1
        if currd>1:
            currarr.append(currd)
        total.append(currarr)
combinations(sequences)
print(total)



#indicies of tiles in first row: [[], [10], [8], [7], [7, 10], [6], [6, 10], [5], [5, 10], [5, 8], [4], [4, 10], [4, 8], [4, 7], [4, 7, 10], [3], [3, 10], [3, 8], [3, 7], [3, 7, 10], [3, 6], [3, 6, 10], [2], [2, 10], [2, 8], [2, 7], [2, 7, 10], [2, 6], [2, 6, 10], [2, 5], [2, 5, 10], [2, 5, 8], [0], [0, 10], [0, 8], [0, 7], [0, 7, 10], [0, 6], [0, 6, 10], [0, 5], [0, 5, 10], [0, 5, 8], [0, 4], [0, 4, 10], [0, 4, 8], [0, 4, 7], [0, 4, 7, 10], [0, 3], [0, 3, 10], [0, 3, 8], [0, 3, 7], [0, 3, 7, 10], [0, 3, 6], [0, 3, 6, 10]]