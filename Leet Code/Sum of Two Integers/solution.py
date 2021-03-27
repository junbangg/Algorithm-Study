class Solution:
    def getSum(self, a: int, b: int) -> int:
        def add(a_bits, b_bits):
            result = []
            carried, count = 0, 0
            limit = 31
            while 1:
                if a_bits[limit] == 1:
                    break
                limit -= 1
            limit += 2
            # addition 
            for i,j in zip(a_bits, b_bits):
                if positive and count == limit:
                    carried = 0
                cur = i ^ j
                result.append(cur ^ carried)
                if i == j == 1 or cur == carried == 1:
                    carried = 1
                else:
                    carried = 0
                count += 1
            return result                
        def copyBits(bits):
            copied = []
            for _ in range(32):
                copied.append(bits & 1)
                bits = bits >> 1
            return copied
        positive, negative = False, False
        #Check negative vs positive
        a, b = max(a, b), min(a, b)
        if a > 0 and b > 0:
            positive = True
        if a < 0 and b < 0:
            negative = True
            a, b = ~a + 1, ~b + 1
        # copy bits to lists
        a_bits = copyBits(a)
        b_bits = copyBits(b)
        # reverse bits in case of negatives
        # empty list for results
        result = add(a_bits, b_bits) 
        # if negative convert two component
        print(result)
        answer = 0            
        while result:
            answer = answer << 1
            answer += result.pop()
        return -abs(answer) if negative else answer 
