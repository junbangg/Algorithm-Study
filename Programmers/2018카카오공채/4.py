def solution(dartResult):
    answer = []
    numString = ''
    num = 0
    skill = False
    for i, v in enumerate(dartResult):
        if v.isdigit():
            if i != 0 and skill:
                answer.append(num)
                skill = False
            numString += v
        else:
            if not skill:
                num = int(numString)
                numString = ''
            skill = True
            if v == 'D':
                num = pow(num, 2)
            if v == 'T':
                num = pow(num, 3)
            if v == '*':
                if answer:
                    answer[-1] *= 2
                num *= 2
            if v == '#':
                num -= 2*num
        print(answer)
    answer.append(num)
    return sum(answer)

testCase = '1D2S#10S'
print(solution(testCase))
