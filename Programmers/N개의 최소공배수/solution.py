import math
def solution(arr):
    def LCM(a, b):
        return abs(a*b) // math.gcd(a,b)
    answer = arr[0]
    for i in range(1, len(arr)):
        cur = arr[i]
        answer = LCM(answer, cur)
    return answer
