# 1. all combinations that add 5
# 2. all combinations of indexes up to 5

import itertools
from itertools import combinations

candidates = []
def findCombinationsUtil(arr, index, num,
                              reducedNum):

    if (reducedNum < 0):
        return
 
    if (reducedNum == 0):
 
        candidates.append(arr)
        return
 
    prev = 1 if(index == 0) else arr[index - 1]
 
    for k in range(prev, num + 1):
         
        arr[index] = k
 
        findCombinationsUtil(arr, index + 1, num,
                                 reducedNum - k)
 
def findCombinations(n):
     
    arr = [0] * n
    # find all combinations
    findCombinationsUtil(arr, 0, n, n)
    print(candidates)
    
 
# Driver code
n = 5
findCombinations(n)


a = list(combinations([i for i in range(10)], 5))
print(a)