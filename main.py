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
#print(total)

def perms(groups):
    return sum(prod(counts[d] for d in group) for group in groups)

#print(perms(total))


#100,000^2- 316,227^2 for 11 digit squares



#generates array of all squares n digits long
def generate_squares(n):
    dranges = {2:[4,9], 3:[10,31], 4:[32,99], 5:[100,316], 6:[317,999], 7:[1000,3162], 8:[3163,9999], 9:[10000,31622], 10: [31623,99999], 11: [100000,316227]}
    return [i*i for i in range(dranges[n][0],dranges[n][1]+1)]

#assuming row 1 is [11]
#assuming row 2 is [11]

def all_same_except_at(n, ignore_indices):
    s = str(n)
    base = next((s[i] for i in range(len(s)) if i not in ignore_indices), None)
    return all(s[i] == base for i in range(len(s)) if i not in ignore_indices)

def testchecker(row1spacing,row1config,row2config):
    usefulnumbers = generate_squares(11)
    res = []
    ignores = []
    for num in usefulnumbers:
        if all_same_except_at(num,[]):
            res.append(num)
    return res

print(testchecker(1,2,3))

        
    
    







#2. validation function:
#example row 1 valid spacings:[[11], [10], [8, 2], [7, 3]. aka an 11 digit square, a 10 digit square followed by a tile / a tile and then a 10 digit square,
# an 8 digit square then a tile then a 2 digit square, etc...
#the function will function take in this list of spacings ([11], [10], [8, 2], [7, 3],etc).
#the function calls function GEN(11) which returns a list of 11 digit numbers in this case.
#example row 2 valid spacings:[[11], [10], [8, 2], [7, 3],etc.
#checks each number from this list of 11 digits numbers that are all squares such as 1121111113111, 1111111211112, etc. against each row 2 spacings to see if its possible to be valid.
# 1121111113111 againnst row2 being [11]: everything in row1 would have to be the same so no invalid
# 1111111211112 againnst row2 being [11]: everything in row1 would have to be the same so no invalid
# 4444444444444 againnst row2 being [11]: VALID SOLUTION.
#etc etc check all of these 11's aginst [11]

#now repeat process for every row1 spacing against every row 2 spacing for example in the [8,2] case:
#generate all 8 digit squares, generate all 2 digit squares.
#row 1 possiblities would look like ABCDEFGH TILE JK where ABCDEFGH is a square and JK is a square. each letter represents a digit btw just for demonstration purposes and shi

# check the solution of the form ABCDEFGH TILE JK against row 2 being[11]. since row 2 is [11], A-G and K must all be the same number. H and J can be different bc theyre the only ones next to tiles. validate this for every possible ABCDEFGH TILE JK number
# then check every ABCDEFGH TILE JK against row 2 being[6,4] for example. in that case, G, H J could be different. H and J can be different same reason as before bc of the tile in row 1. G can be different bc its directly bove the tile in row 2. the rest all have to be same.
#etc etc etc i hope u understand basically for each valid row1 spacing generate each possible ACTUAL SOLUTION. then check if that solution is theoretically possible by checking if all digits in the entire solution are the same, except digits that are to the left/right of a tile in row1 or above a tile in row 2 CAN be different. emphasis on can, they could still be the same.

                   


