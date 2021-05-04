
def solution(stones, k):
    def check(mid, k):
        p1, p2 = 0, 0
        for stone in stones:
            if stone - mid <= 0:
                p2 += 1
            else:
                p2 += 1
                p1 = p2
            if p2 - p1 >= k:
                return True
        return False
            
    left, right = 1, 200000000
    while left <= right:
        mid = left + (right - left) // 2
        if check(mid, k):
            right = mid - 1
        else:
            left = mid + 1
    
    return left
