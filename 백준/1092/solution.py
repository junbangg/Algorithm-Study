N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)
# edge case
if cranes[0] < boxes[0]:
    print(-1)
    exit(0)

crane_box = [0] * N
checked = [False] * M

count, time = 0, 0
boxLength = len(boxes)
while True:
    if count == boxLength:
        break
    for i in range(N):
        while crane_box[i] < boxLength:
            if not checked[crane_box[i]] and boxes[crane_box[i]] <= cranes[i]:
                checked[crane_box[i]] = True
                crane_box[i] += 1
                count += 1
                break
            crane_box[i] += 1
    time += 1
print(time)