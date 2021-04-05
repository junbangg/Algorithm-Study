# Recursion Solution
class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        return self.fib(n-2) + self.fib(n-1)

# Memoization Solution
class Solution:
    def fib(self, n: int) -> int:
        dp = collections.defaultdict(int)
        def recurse(n):
            if n <= 1:
                return n
            if dp[n] == 0:
                dp[n] = recurse(n - 2) + recurse(n - 1)
            return dp[n]
        return recurse(n)
