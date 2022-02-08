import sys

input = sys.stdin.readline

N = int(input())
totalPeople = 0
houses = []

for _ in range(N):
    index, people = map(int, input().split())
    totalPeople += people
    houses.append((index, people))

peopleCount = 0
for index, people in sorted(houses, key = lambda x: x[0]):
    peopleCount += people
    if peopleCount > totalPeople//2:
        print(index)
        break

