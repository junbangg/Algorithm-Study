# return the nth number in the Fibonacci Sequence
'''
0 1 1 2 3 5 8 13 21 34 55
F(2) = F(1) + F(0)
1  = 1 + 0

F(5) = F(4) + F(3) + F(2) + F(1) + F(0)

F(n) = F(n-1) + F(n-2)
'''
# O(2^n)
def fibonacci(n):
    #base case
    dp = {}
    def recurse(n):
        if n <= 1:
            return n
        if n in dp:
            return dp[n]
        dp[n] = recurse(n-1) + recurse(n-2)
        return dp[n]
    return recurse(n)
'''
0 1 1 2 3 5 8
dp[0] = 0
dp[1] = 1

2 -> n
dp[n] = dp[n-1] + dp[n-2]
'''
def fibonacci_iterative(n):
    dp = {}
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fibonacci_iterative(10))
