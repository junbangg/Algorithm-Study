k, n = list(map(int, input().split()))
lans = [int(input()) for _ in range(k)]


def cut(pivot):
    total = 0
    for lan in lans:
        total += lan // pivot
    return total

left, right = 1, max(lans)
answer = 0
while left <= right:
    pivot = left + (right - left) // 2
    pieces = cut(pivot)
    if pieces >= n:
        answer = pivot
        left = pivot + 1
    else:
        right = pivot - 1
print(answer)

