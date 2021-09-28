import sys, math
input = sys.stdin.readline
N = int(input())

# def checkPrime(n):
#     if n == 2:
#         return True
#     if n % 2 == 0 or n <= 1:
#         return False

#     sqr = int(math.sqrt(n)) + 1

#     for divisor in range(3, sqr, 2):
#         if n % divisor == 0:
#             return False
#     return True

# primes = [i for i in range(N+1) if checkPrime(i)]

def sieve(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    nums = []
    for p in range(n + 1):
        if prime[p]:
            nums.append(p)
    return nums

# 1~N 까지의 모든 소수 구하기
# 슬라이딩 윈도우로 연속해서 N 이 되면 answer ++ 
# 

# 41 : 2+3+5+7+11+13 = 11+13+17 = 41 (세 가지)

# 2, 3, 5, 7, 11, 13, 17
# [2] != 41 and < 41:
#    [2] <- 3
# [2, 3] != 41 and < 41:
#     [2, 3] <- 5
# [2, 3, 5] != 41 and < 41:
# ...
# [2, 3, 5, 7, 11, 13] == 41:
#     answer ++
# [3] 부터 시작

primes = sieve(N)
answer = 0
# answers = []
for i in range(len(primes)):
    _sum = primes[i]
    # temp = [primes[i]]
    ptr = i + 1
    while ptr < len(primes) and _sum != N:
        _sum += primes[ptr]
        # temp.append(primes[ptr])
        ptr += 1

    if _sum == N:
        answer += 1
        # answers.append(temp)
print(answer)
# print(answers)

