N = int(input())
budget = list(map(int, input().split()))
M = int(input())

def calculate(pivot):
    total = 0
    for num in budget:
        if num > pivot:
            total += pivot
        else:
            total += num
    return total


left, right = 0, max(budget)
answer = 0
while left <= right:
    pivot = left + (right - left) // 2
    total = calculate(pivot)
    if total <= M:
        answer = pivot
        left = pivot + 1
    else:
        right = pivot - 1

print(answer)
