def solution(arr):
    answer, current = 0, arr[0]
    if current > 0:
        answer += 1
    for i in range(1, len(arr)):
        current += arr[i]
        if current > 0:
            answer += 1
    return answer
