N, C = map(int, input().split())
points = sorted([int(input()) for _ in range(N)])
answer = set()
# edge case
if C == 2:
    print(points[-1] - points[0])

def binarySearch(left, right, x, y):
    # left
    ll, lr = left, right
    lcount = 0
    while ll <= lr:
        pivot = ll + (lr - ll) // 2
        if lcount <= x:
            answer.add(points[pivot])
            lcount += 1
            right = pivot - 1
        else:
            break
    # right
    rl, rr = left, right
    rcount = 0
    while rl <= rr:
        pivot = rl + (rl - rr) // 2
        if rcount <= y:
            answer.add(points[pivot])
            rcount += 1
            left = pivot + 1
        else:
            break

x, y = C // 2, C - C // 2

binarySearch(0, len(points)-1, x+1, y+1)
print(answer)
