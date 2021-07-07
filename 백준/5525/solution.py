N = int(input())
M = int(input())
S = input()
answer = i = count = 0
while i < M-1:
    if S[i-1:i+2] == 'IOI':
        count += 1
        if count == N:
            answer += 1
            count -= 1
        i += 1
    else:
        count = 0
    i += 1

print(answer)
