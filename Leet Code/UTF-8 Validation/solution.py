class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(size):
            for i in range(start + 1, start + size + 1):
                if i >= len(data) or data[i] >> 6 != 0b10:
                    return False
            return True
        start = 0
        while start < len(data):
            first = data[start]
            if first >> 3 == 0b11110 and check(3):
                start += 4
            elif first >> 4 == 0b1110 and check(2):
                start += 3
            elif first >> 5 == 0b110 and check(1):
                start += 2
            elif first >> 7 == 0:
                start += 1
            else:
                return False
        return True

# retried solution
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def checkCount(nxt, count):
            tens = 0
            for i in range(nxt + 1, nxt + count):
                byte = bin(data[i])[2:].zfill(8)
                if byte[:2] == '10':
                    tens += 1
            if tens == count - 1:
                return True
            return False
        i = 0
        while i < len(data):
            byte = bin(data[i])[2:].zfill(8)
            if byte[:3] == '110' and i + 2 <= len(data) and checkCount(i, 2) :
                i += 2 
            elif byte[:4] == '1110' and i + 3 <= len(data) and checkCount(i, 3):
                i += 3 
            elif byte[:5] == '11110' and i + 4 <= len(data) and checkCount(i, 4):
                i += 4 
            elif byte[0] == '0':
                i += 1
            else:
                return False
        return True
