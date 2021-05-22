'''
a = [4,5,6,5,4,3]

key : val
 4 : 2
 5 : 2
 6 : 1
 3 : 1

 1 - > [3, 6]
 2 -> [4, 5]

 [3, 6, 4, 4, 5, 5]
 '''

import collections, heapq
def sortByCount(nums):
    # edge case
    if not nums:
        return nums
    answer = []
    # count
    count = collections.Counter(nums)
    heapDic = collections.defaultdict(list)
    for key, val in count.items():
        heapq.heappush(heapDic[val], key)
    for key, h in heapDic.items():
        while h:
            answer.append(heapq.heappop(h))
    return answer

a = [4,5,6,5,4,3]
print(sortByCount(a))
