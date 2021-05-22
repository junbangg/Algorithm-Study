
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
# pythonic solution: O(nlogn)
def sortByCountImproved(nums):
    count = collections.Counter(nums)
    return sorted(nums, key = lambda x: (count[x], x))

# quickSort solution : O(nlogn)
def quickSort(nums, count, low, high):
    def partition(nums, low, high):
        left, pivot = low, nums[high]
        for right in range(low, high):
            if count[nums[right]] < count[pivot]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            elif count[nums[right]] == count[pivot] and nums[right] < pivot:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        nums[left], nums[high] = nums[high], nums[left]
        return left
    if low < high:
        p = partition(nums, low, high)
        quickSort(nums, count, low, p-1)
        quickSort(nums, count, p+1, high)
    return nums
def solution(nums):
    if not nums:
        return nums
    count = collections.Counter(nums)
    return quickSort(nums, count, 0, len(nums)-1)
a = [4,5,6,5,4,3]
print(solution(a))
