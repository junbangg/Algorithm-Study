# regular prime function
def checkPrime(n):
    if n>1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

# optimized prime function
def optimusPrime(n):
    if n & 1 == 0:
        return 2
    d= 3
    while d * d <= n:
        if n % d == 0:
            return d
        d= d + 2
    return 0

def solution1(n):
    return sum(map(lambda x: x == 0, [optimusPrime(i) for i in range(1, n+1)]))



# Sieve of Eratosthenes

def solution2(n):
    nums = set(range(2, n+1))
    for i in range(2, n+1):
        if i in nums:
            nums -= set(range(2*i, n+1, i))
    return len(nums)



