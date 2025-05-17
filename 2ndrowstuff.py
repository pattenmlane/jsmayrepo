from math import prod
invalid_squares = [1,4,5,9]
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
print(ones(sequences))

#indicies of 