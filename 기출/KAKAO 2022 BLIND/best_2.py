def checkPrime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):

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

def convertTo(base, inputNum):
    res = ""
    index = 0

    while (inputNum > 0):
        res += calc(inputNum % base)
        inputNum = int(inputNum / base)

    res = res[::-1]
    return res

def hasZero(num):
    return '0' in num

def solution(n, k):
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
    # P 
    if not hasZero(number):
        if checkPrime(int(number)):
            answer += 1

    for ind, c in enumerate(candidates):
        # 소수 확인
        if not checkPrime(int(c)) or hasZero(c):
            continue
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

