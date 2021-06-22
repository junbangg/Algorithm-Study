n = int(input())
six = 666
count = 0
while True:
    if '666' in str(six):
        count += 1
    if count == n:
        print(six)
        break
    six += 1
