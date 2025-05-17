### [1,1,1,1,1,1,T,1,1,1,T]
from itertools import product
def all_same_except_at(seq, ignore_indices, ignore_value='T'):
    reference = None
    for i, val in enumerate(seq):
        if i in ignore_indices or val == ignore_value:
            continue
        if reference is None:
            reference = val
        elif val != reference:
            return False
    return True

#print(all_same_except_at([1,1,1,1,1,1,'T',1,1,1,"T"],[2]))



order = [6,4,5]

squares = {6:['a','b','c'],4:['d','e','f'],5:['g','h'] }
r1solutions = []
for combo in product(*(squares[k] for k in order)):
    r1solutions.append(combo)
print(r1solutions)

print(min(['8', '1', '8', '1', '8', '4', '1'])*3)