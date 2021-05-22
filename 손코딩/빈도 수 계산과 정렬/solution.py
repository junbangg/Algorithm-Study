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
    # create heapDic
    # O(nlogn)
    for num in nums:
        heapq.heappush(heapDic[count[num]], num)
    # O(keyLength * key-heap) O(n2)
    for key, h in heapDic.items():
        while h:
            answer.append(heapq.heappop(h))
    return answer

def sortByCountImproved(nums):
    count = collections.Counter(nums)
    return sorted(nums, key = lambda x: (count[x], x))



a = [4,5,6,5,4,3]
print(sortByCountImproved(a))
