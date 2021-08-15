import sys
input = sys.stdin.readline
word = list(input().rstrip())
i = start = 0

while i < len(word):
    # <
    if word[i] == '<':
        while word[i] != '>':
            i += 1
    # word
    if word[i].isalnum():
        start = i
        while i < len(word) and word[i].isalnum():
            i += 1
        temp = word[start:i][::-1]
        word[start:i] = temp
    else:
        i += 1
print(''.join(word))