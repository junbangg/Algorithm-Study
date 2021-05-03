def solution(inputString):
    stack = []
    table = {')': '(',
             '}': '{',
             ']': '[',
             '>': '<'}
    parentheses = '({[<)}]>'
    correct = 0
    incorrect = []
    #edge case
    if inputString[0] in table or inputString[0] not in parentheses:
        return 0
    #check for parentheses
    for i, char in enumerate(s):
        if char not in parentheses:
            continue
        elif char not in table:
            if i >= 2:
                return -abs(i)
            else:
                correct += 1
                stack.append(char, i)
        elif not stack or table[char] != stack[-1][0]:
            p, ind = stack.pop()
            incorrect.append(-ind)
        else:
            stack.pop()
            correct += 1
    if not incorrect:
        return correct
    return incorrect[0]

test = 'Hello, world!'
