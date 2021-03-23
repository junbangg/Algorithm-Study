enter = [1,4,2,3]
leave = [2,1,3,4]
output = [2,2,1,3]

from collections import defaultdict
from itertools import permutations

def solution(enter, leave):
    answer = [0] * len(enter)
    indexes = defaultdict(list)
    permuts = permutations(enter, 2)
    for index, value in enumerate(enter):
        indexes[value].append(index)
    for index, value in enumerate(leave):
        indexes[value].append(index)
    print(indexes)
    for per in permuts:
        a, b = per[0], per[1]
        boolEnter = indexes[a][0] > indexes[b][0]
        boolLeave = indexes[a][1] > indexes[b][1]
        print("{},{}->{})".format(a, b, boolEnter == boolLeave))
        if boolEnter != boolLeave:
            answer[a-1] += 1
    return answer

print(solution(enter, leave))


