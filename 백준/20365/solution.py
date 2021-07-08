N = int(input())
colors = input()
B = colors.count('B')
R = colors.count('R')
target = ''
if B <= R:
    target = 'B'
else:
    target = 'R'

left, count = 0, 1
while left < len(colors):
    if colors[left] == target:
        right = left
        while right < len(colors) and colors[right] == target:
            right += 1
        left = right
        count += 1
    left += 1
print(count)