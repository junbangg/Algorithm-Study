# Difficult Solution
class Solution:
    def reverseBits(self, n):
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n

# Intuitive Solution
class Solution:
    def reverseBits(self, n):
        # Save reversed Bits to list
        bitList = []
        for _ in range(32):
            bitList.append(n&1)
            n = n >> 1
        # Reverse List
        bitList = bitList[::-1]
        # pop() bits to create new integer
        result = 0
        while bitList:
            result = result << 1
            result += bitList.pop()
        return result
