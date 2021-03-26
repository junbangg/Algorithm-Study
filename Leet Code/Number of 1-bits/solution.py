class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

# Bit Manipulation Solution
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
