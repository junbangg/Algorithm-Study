import sys, collections
input = sys.stdin.readline
N = int(input())
dic = collections.defaultdict(list)
priority = []
# 그냥 정렬로 최적화 시도
words = []
for _ in range(N):
    letters = input().rstrip()
    words.append(letters)
    length = len(letters)
    for c in letters:
        priority.append([length, c])
        length -= 1
priority.sort(reverse=True)
# letter_num = collections.defaultdict(int)
letter_num = {}
num = 9
for _, letter in priority:
    # if letter_num[letter] == 0:
    if letter not in letter_num:
        letter_num[letter] = num
        num -= 1

answer = 0
for word in words:
    answer += int(''.join(str(letter_num[c]) for c in word).rstrip())
print(answer)




    





