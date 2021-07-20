import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
S = int(input())
students = list(map(int, input().split()))

scores = []
photos = []
# number, index
for time, student in enumerate(students):
    # 사진틀에 있으면
    if student in photos:
        for i, pic in enumerate(photos):
            if student == pic:
                scores[i] += 1
    # 사진 틀에 없으면
    else:
        if len(photos) >= N:
            minScore = min(scores)
            for i, pic in enumerate(photos):
                if scores[i] == minScore:
                    del photos[i]
                    del scores[i]
                    break
        photos.append(student)
        scores.append(1)
photos.sort()
print(*photos)


