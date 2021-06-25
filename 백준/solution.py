# 10773
n = int(input())

total, stack = 0, []
for _ in range(n):
    num = int(input())
    if num == 0:
        total -= stack.pop()
    else:
        total += num
        stack.append(num)
print(total)




