import sys
input = sys.stdin.readline

# function for calculating distance
def getDistance(x, y, target_x, target_y):
    return abs(x-target_x)+ abs(y-target_y)
# keyboard
keyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
            ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
vowels = 'yuiophjklbnm'
# input
left, right = input().split()
word = input().rstrip()

# letter positions
letterMap = {}
for x in range(len(keyboard)):
    for y in range(len(keyboard[x])):
        letterMap[keyboard[x][y]] = (x, y)

# find coordinates of left and right
left_x ,left_y = letterMap[left]
right_x, right_y = letterMap[right]

# main
answer = 0
for c in word:
    answer += 1
    nxt_x, nxt_y = letterMap[c]
    #right
    if c in vowels:
        answer += getDistance(right_x, right_y, nxt_x, nxt_y)
        right_x, right_y = nxt_x, nxt_y
    else:
        answer += getDistance(left_x, left_y, nxt_x, nxt_y)
        left_x, left_y = nxt_x, nxt_y
print(answer)