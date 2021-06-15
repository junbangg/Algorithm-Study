n = int(input())
ox = input()
total, bonus = 0, 0
for i, v in enumerate(ox):
    if v == 'O':
        total += i + 1 + bonus
        bonus += 1
    else:
        bonus = 0
print(total)
