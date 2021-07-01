import sys
N = int(sys.stdin.readline())
words = [sys.stdin.readline()[:-1] for _ in range(N)]

edited = []
for word in words:
    newWord = []
    nums = []
    numCount = 0
    for c in word:
        if c.isnumeric():
            if not nums and c == '0':
                numCount += 1
            else:
                nums.append(c)
        else:
            if nums:
                newWord.append((''.join(nums), numCount))
                nums = []
                numCount = 0
            lower = 0
            if c.islower():
                lower = 1
            newWord.append((lower(c), lower, c))
    if nums:
        newWord.append(nums)
    edited.append(newWord)
print(edited)
