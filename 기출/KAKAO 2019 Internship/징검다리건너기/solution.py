# 반복문 버전
# 효율성 TC 하나 미통과
def check(mid, stones, k):
    left = right = 0
    for stone in stones:
        if stone - mid <= 0:
            right += 1
        else:
            right += 1
            left = right
        if right - left >= k:
            return False
    return True

def solution(stones, k):
    answer = 0
    left, right = 1, max(stones)
    while left <= right:
        mid = left + (right - left) // 2
        if check(mid, stones, k):
            left = mid + 1
        else:
            right = mid - 1
    return left

# 재귀버전
# 통과

def check(mid, stones, k):
    left = right = 0
    for stone in stones:
        if stone - mid <= 0:
            right += 1
        else:
            right += 1
            left = right
        if right - left >= k:
            return False
    return True

def binarySearch(left, right, stones, k):
    if left > right:
        return left
    mid = left + (right - left) // 2
    if check(mid, stones, k):
        return binarySearch(mid + 1, right, stones, k)
    else:
        return binarySearch(left, mid - 1, stones, k)

def solution(stones, k):
    answer = 0
    left, right = 1, 200000000
    
    return binarySearch(left, right, stones, k)