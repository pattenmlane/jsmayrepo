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



backtracking([])
#print(len(sequences))


def count_prod20(n):
    if n<2:
        return 0
    
    case_45 = n*(n-1)
    case_225 =0 if n<3 else n* (n-1) * (n-2) //2

    return case_45 + case_225

counts={}

for n in range(2,12):
    counts[n] = count_prod20(n)

#print(counts)


total=[]
#print(sequences)
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

def perms(groups):
    return sum(prod(counts[d] for d in group) for group in groups)

print(perms(total))


#11
#10
#9
#8


#100,000- 316,227

print(316227*316227)


