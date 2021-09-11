# 소수를 다 찾고 조건 확인을 할지
# 소수를 하나의 조건으로 생각할지

# 1. k 진수로 바꾸기 구현
# 2. 0이 아닌 모든 수 찾기...split by 0?
# 3. 찾은 숫자들에 대해 모든 조건 비교해보기
import sys
def checkPrime(num):
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
 
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False
        

def calc(num):
 
    if (num >= 0 and num <= 9):
        return chr(num + ord('0'))
    else:
        return chr(num - 10 + ord('A'))
 
# Function to convert a given decimal
# number to a base 'base' and
def convertTo(base, inputNum):
    res = ""
    index = 0 # Initialize index of result
 
    # Convert input number is given base
    # by repeatedly dividing it by base
    # and taking remainder
    while (inputNum > 0):
        res += calc(inputNum % base)
        inputNum = int(inputNum / base)
 
    # Reverse the result
    res = res[::-1]
    return res

def hasZero(num):
    return '0' in num

 #틀리면, 모든 0을 추가해주자..tc2 확인
def solution(n, k):
    number = n
    if k != 10:
        number = convertTo(k, n)
    candidates = []
    temp = ''
    for i, v in enumerate(number):
        if v == '0' and temp:
            candidates.append(temp)
            candidates.append('0')
            temp = ''
        elif v != '0':
            temp += v
    if temp:
        candidates.append(temp)
    
    answer = 0
    if not hasZero(number):
        if len(number) <= sys.maxsize and checkPrime(int(number)):
            answer += 1

    for ind, c in enumerate(candidates):
        # 소수 확인
        if not checkPrime(int(c)) or hasZero(c):
            continue
        # if not checkPrime(int(c)):
            # continue
        # OPO
        if ind > 0 and ind < len(candidates) - 1 and candidates[ind-1] == '0' and candidates[ind+1] == '0':
            answer += 1
            continue
        # PO
        if ind < len(candidates) - 1 and candidates[ind+1] == '0':
            answer += 1
            continue
        # OP
        if ind > 0 and candidates[ind-1] == '0':
            answer += 1
            continue

    return answer

tc1 = [437674, 3]
tc2 = [110011, 10]
print(solution(tc1[0], tc1[1]))
