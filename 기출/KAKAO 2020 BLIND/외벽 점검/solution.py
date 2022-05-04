from itertools import permutations

def solution(n, weak, dist):
    weakSize = len(weak)
    weak = weak + [w + n for w in weak]
    minCount = float('inf')
    for start in range(weakSize):
        for friends in permutations(dist, len(dist)):
            friendPointer = 1
            currentPointer = start
            # next pointer
            for i in range(1, weakSize):
                nextPointer = start + i
                diff = weak[nextPointer] - weak[currentPointer]
                if diff > friends[friendPointer-1]:
                    currentPointer = nextPointer
                    friendPointer += 1
                    if friendPointer > len(friends):
                        break
            if friendPointer <= len(friends):
                minCount = min(minCount, friendPointer)
    return -1 if minCount == float('inf') else minCount