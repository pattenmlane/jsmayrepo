from itertools import product
import copy
###########HELPERS############

### [1,1,1,1,1,1,T,1,1,1,T]
def all_same_except_at(seq, ignore_indices, ignore_value='T'):
    n = len(seq)
    # Build a set of indices to ignore: explicitly ignored + adjacent to any 'T'
    dynamic_ignores = set(ignore_indices)
    for i, val in enumerate(seq):
        if val == ignore_value:
            if i > 0:
                dynamic_ignores.add(i - 1)
            if i < n - 1:
                dynamic_ignores.add(i + 1)
    
    reference = None
    for i, val in enumerate(seq):
        if i in dynamic_ignores or val == ignore_value:
            continue
        if reference is None:
            reference = val
        elif val != reference:
            return False
    return True

print()
def generate_squares(n):
    dranges = {2:[4,9], 3:[10,31], 4:[32,99], 5:[100,316], 6:[317,999], 7:[1000,3162], 8:[3163,9999], 9:[10000,31622], 10: [31623,99999], 11: [100000,316227]}
    return [i*i for i in range(dranges[n][0],dranges[n][1]+1)]

def exceptatgenerator(arr):
    res = []
    for num in arr:
        if num-1>=0:
            res.append(num-1)
        if num+1<11:
            res.append(num+1)
    return res
        





#####MAIN CHECKING FUNCTION########


#row 1:#indicies of tiles in first row: [[], [10], [8], [7], [7, 10], [6], [6, 10], [5], [5, 10], [5, 8], [4], [4, 10], [4, 8], [4, 7], [4, 7, 10], [3], [3, 10], [3, 8], [3, 7], [3, 7, 10], [3, 6], [3, 6, 10], [2], [2, 10], [2, 8], [2, 7], [2, 7, 10], [2, 6], [2, 6, 10], [2, 5], [2, 5, 10], [2, 5, 8], [0], [0, 10], [0, 8], [0, 7], [0, 7, 10], [0, 6], [0, 6, 10], [0, 5], [0, 5, 10], [0, 5, 8], [0, 4], [0, 4, 10], [0, 4, 8], [0, 4, 7], [0, 4, 7, 10], [0, 3], [0, 3, 10], [0, 3, 8], [0, 3, 7], [0, 3, 7, 10], [0, 3, 6], [0, 3, 6, 10]]
#row2: [[], [10], [8], [7], [7, 10], [6], [6, 10], [3], [3, 10], [3, 8], [3, 7], [3, 7, 10], [3, 6], [3, 6, 10], [2], [2, 10], [2, 8], [2, 7], [2, 7, 10], [2, 6], [2, 6, 10], [0], [0, 10], [0, 8], [0, 7], [0, 7, 10], [0, 6], [0, 6, 10], [0, 3], [0, 3, 10], [0, 3, 8], [0, 3, 7], [0, 3, 7, 10], [0, 3, 6], [0, 3, 6, 10]]
#usefulrow1numbers:[[11], [10], [8, 2], [7, 3], [7, 2], [6, 4], [6, 3], [5, 5], [5, 4], [5, 2, 2], [4, 6], [4, 5], [4, 3, 2], [4, 2, 3], [4, 2, 2], [3, 7], [3, 6], [3, 4, 2], [3, 3, 3], [3, 3, 2], [3, 2, 4], [3, 2, 3], [2, 8], [2, 7], [2, 5, 2], [2, 4, 3], [2, 4, 2], [2, 3, 4], [2, 3, 3], [2, 2, 5], [2, 2, 4], [2, 2, 2, 2], [10], [9], [7, 2], [6, 3], [6, 2], [5, 4], [5, 3], [4, 5], [4, 4], [4, 2, 2], [3, 6], [3, 5], [3, 3, 2], [3, 2, 3], [3, 2, 2], [2, 7], [2, 6], [2, 4, 2], [2, 3, 3], [2, 3, 2], [2, 2, 4], [2, 2, 3]]


def testchecker(row1tiles,row2tiles,row1squarelengths):
    bigboypossibleresults = {}
    
    for j, spacingset in enumerate(row1squarelengths):
        
        squares = {}
        
        for num in spacingset:
            squares[num] = generate_squares(num)
        
        order = spacingset
        r1solutions = []

        for combo in product(*(squares[k] for k in order)):
            r1solutions.append(combo)
        
        
        ####downward
        for solution in r1solutions:
            finalarray = [0]*11
            
            for tile in row1tiles[j]:
                finalarray[tile] = 'T'
            count = 0
            
            for bs in solution:
                
                for char in str(bs):

                    if finalarray[count] != 'T':
                        finalarray[count] = char
                        count+=1
                    else:
                        finalarray[count+1] = char
                        count+=2
            
            
            for row2bs in row2tiles:###maybe check
                ignores = row2bs
                

                if all_same_except_at(finalarray,ignores):
                    
                    if tuple(row2bs) in bigboypossibleresults:
                        bigboypossibleresults[tuple(row2bs)].append(finalarray)
                    else:
                        bigboypossibleresults[tuple(row2bs)] = [finalarray]
    
    return bigboypossibleresults


a = [[], [10], [8], [7], [7, 10], [6], [6, 10], [5], [5, 10], [5, 8], [4], [4, 10], [4, 8], [4, 7], [4, 7, 10], [3], [3, 10], [3, 8], [3, 7], [3, 7, 10], [3, 6], [3, 6, 10], [2], [2, 10], [2, 8], [2, 7], [2, 7, 10], [2, 6], [2, 6, 10], [2, 5], [2, 5, 10], [2, 5, 8], [0], [0, 10], [0, 8], [0, 7], [0, 7, 10], [0, 6], [0, 6, 10], [0, 5], [0, 5, 10], [0, 5, 8], [0, 4], [0, 4, 10], [0, 4, 8], [0, 4, 7], [0, 4, 7, 10], [0, 3], [0, 3, 10], [0, 3, 8], [0, 3, 7], [0, 3, 7, 10], [0, 3, 6], [0, 3, 6, 10]]
b = [[], [10], [8], [7], [7, 10], [6], [6, 10], [3], [3, 10], [3, 8], [3, 7], [3, 7, 10], [3, 6], [3, 6, 10], [2], [2, 10], [2, 8], [2, 7], [2, 7, 10], [2, 6], [2, 6, 10], [0], [0, 10], [0, 8], [0, 7], [0, 7, 10], [0, 6], [0, 6, 10], [0, 3], [0, 3, 10], [0, 3, 8], [0, 3, 7], [0, 3, 7, 10], [0, 3, 6], [0, 3, 6, 10]]
c = [[11], [10], [8, 2], [7, 3], [7, 2], [6, 4], [6, 3], [5, 5], [5, 4], [5, 2, 2], [4, 6], [4, 5], [4, 3, 2], [4, 2, 3], [4, 2, 2], [3, 7], [3, 6], [3, 4, 2], [3, 3, 3], [3, 3, 2], [3, 2, 4], [3, 2, 3], [2, 8], [2, 7], [2, 5, 2], [2, 4, 3], [2, 4, 2], [2, 3, 4], [2, 3, 3], [2, 2, 5], [2, 2, 4], [2, 2, 2, 2], [10], [9], [7, 2], [6, 3], [6, 2], [5, 4], [5, 3], [4, 5], [4, 4], [4, 2, 2], [3, 6], [3, 5], [3, 3, 2], [3, 2, 3], [3, 2, 2], [2, 7], [2, 6], [2, 4, 2], [2, 3, 3], [2, 3, 2], [2, 2, 4], [2, 2, 3]]

yay = testchecker(a,b,c)



reallifesolutions = []

    
for key in yay:

    for sol in yay[key]:
        cc = copy.deepcopy(sol)
        cc.pop(1)
        minn = int(min(v for v in cc if v != 'T'))

        if all(cc[i].isdigit() and int(cc[i]) <= minn * 2 for i in [0, 2, 3, 9]) and all(cc[i].isdigit() and int(cc[i]) <= minn * 3 for i in [1, 4, 5, 6, 7, 8]):
            reallifesolutions.append(sol)
print(len(reallifesolutions))
