from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for i in course:
        candidates = []
        for order in orders:
            candidates.extend(map(lambda x: tuple(sorted(x)), combinations(order, i)))
        if candidates:
            count = Counter(candidates).most_common()
            maxVal = count[0][1]
            if maxVal >= 2:
                for tup in count:
                    if tup[1] == maxVal:
                        answer.append(''.join(tup[0]))
    return sorted(answer)
