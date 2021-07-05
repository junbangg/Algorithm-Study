def solution(arr):
    answer = 0
    left, right = 0, 0
    while left < len(arr):
        cur = arr[left]
        if cur == 0:
            left += 1
        if cur == 1:
            right = left
            while right < len(arr) and arr[right] == 1:
                right += 1
            answer = max(answer, right - left)
            left = right
    return answer
print(solution([0, 1, 0, 1, 1, 1, 0, 1, 1]))
print(solution([1,1,1,1,1,1,1,1,1]))
print(solution([0, 0, 0, 0, 0, 0, 0, 0]))
print(solution([1,0,0,0,1,1,1,1,0,0,1,1,1]))