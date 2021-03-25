# Solution using stacks
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        bits = bits[:-1][::-1]
        b = ''
        while bits:
            b += str(bits.pop())
            if b == '0' or b == '10' or b == '11':
                b = ''
        return b == ''
