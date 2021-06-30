import sys
N, M = map(int, sys.stdin.readline().split())
T = [int(sys.stdin.readline()) for _ in range(N)]

def check(limit):
    count = 0
    for t in T:
        count += limit // t
    if count >= M: return True
    return False

def binarySearch(left, right):
    answer = 0
    while left <= right:
        time = left + (right - left) // 2
        if check(time):
            answer = time
            right = time - 1
        else:
            left = time + 1
    return answer

# max(worst case scenario) is (number of people X biggest time)
left , right = 0, M * max(T)
print(binarySearch(left, right))


