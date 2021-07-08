N = int(input())
colors = input()

def count(target):
    left, count = 0, 1
    while left < len(colors):
        if colors[left] == target:
            right = left
            while right < len(colors) and colors[right] == target:
                right += 1
            left = right
            count += 1
        left += 1
    return count

B = count('B')
R = count('R')
print(min(B,R))