def solution(inputString):
    dic = { ')': '(',
           ']': '[',
           '}': '{',
           '>': '<'}
    stack = []
    # edge case
    if inputString[0] in dic.keys() or inputString[0] in dic.values():
        return 0
    pairs = 0
    for i, p in enumerate(inputString):
        # check opening parentheses
        if p in dic.values():
            stack.append(p)
        # check closing parentheses
        elif p in dic.keys():
            # match with parentheses in stack
            if stack and stack[-1] == dic[p]:
                stack.pop()
                pairs += 1 # increment pairs
            # no match => return index
            else:
                return -i
    # if parentheses remains in stack -> return last char index
    if stack:
        return -(len(inputString) - 1)
    # return pairs
    return pairs



# provided testcases
tc1 = 'Hello, world!' #0
tc2 = 'line [({<plus>)}]' # -14
tc3 = 'line [({<plus>})' # -15
tc4 = '>_<' #0
tc5 = 'x * (y + z) ^ 2 = ?' #1

# custom
tc6 = 'ABC)ABC'


print(solution(tc1))
print(solution(tc2))
print(solution(tc3))
print(solution(tc4))
print(solution(tc5))
print(solution(tc6))
