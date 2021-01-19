def solution(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0]) or [ -1]

# or


def solution(arr, divisor):
    result = [i for i in arr if i % divisor == 0]
    return [-1] if not result else sorted(result)
