from itertools import combinations
from collections import defaultdict

def binarySearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return len(arr) - left
            
def solution(info, query):
    answer = []
    dataMap = defaultdict(list)
    for data in info:
        data = data.split()
        key = data
        dataVal = int(data[-1])
        for i in range(5):
            for comb in combinations(key, i):
                dataKey = ''.join(comb)
                dataMap[dataKey].append(dataVal)
    for key in dataMap:
        dataMap[key].sort()
    # query
    for q in query:
        queryKey = q.split(' and ')
        last, val = queryKey.pop().split()
        queryKey.append(last)
        queryKey = ''.join(queryKey).replace('-', '')
        # binary search
        answer.append(binarySearch(dataMap[queryKey], int(val)))
        
    return answer