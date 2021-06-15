def solution(n, a, b):
    nums = [i for i in range(1, n+1)]
    def recurse(arr, count):
        if len(arr) == 2 and arr[0] == a and arr[1] == b:
            return count
        nxt = []
        for i in range(1, len(arr), 2):
            first, second = arr[i-1], arr[i]
            if first == a or first == b:
                nxt.append(first)
            elif second == a or second == b:
                nxt.append(second)
            else:
                nxt.append(arr[i])
        return recurse(nxt, count+1)
    return recurse(nums, 1)
n = 16
a = 4
b = 10
print(solution(n, a, b))



