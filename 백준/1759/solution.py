import sys
input = sys.stdin.readline
L, C = map(int, input().split())
letters = sorted(input().rstrip().split())

answers = []

def isValid(s):
    vowels = 'aeiou'
    vowel = nonVowel = 0
    for c in s:
        if c in vowels:
            vowel += 1
        else:
            nonVowel += 1
    return vowel >= 1 and nonVowel >= 2

def find(ind, s):
    if len(s) == L:
        if isValid(s):
            answers.append(s)
        return
    for i in range(ind+1, C):
        find(i, s + letters[i])

for i in range(C):
    find(i, letters[i])

for a in answers:
    print(a)