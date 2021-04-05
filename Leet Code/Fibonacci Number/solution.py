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
# Tabulation solution
class Solution:
    dp = collections.defaultdict(int)
    def fib(self, n: int) -> int:
        self.dp[1] = 1
        for i in range(2, n+1):
            self.dp[i] = self.dp[i-2] + self.dp[i-1]
        return self.dp[n]
