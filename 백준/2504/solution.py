params = list(input())
close_open = {')' : '(',
               ']' : '[' }
open_val = {'(' : 2,
            '[' : 3}
stack = []
for p in params:
    # if open
    if p in open_val.keys():
        stack.append(p)
    #if closed
    else:
        val, temp = 0, 0
        # check if not valid
        if not stack or type(stack[-1]) != int and close_open[p] != stack[-1]:
            print('0')
            exit()
        # check if peek == number
        if stack and type(stack[-1]) == int:
            temp += stack.pop()
        # if parentheses matches
        if stack and close_open[p] == stack[-1]:
            nextVal = open_val[stack.pop()]
            if temp > 0:
                nextVal *= temp
            val += nextVal
        # add numbers
        while stack and type(stack[-1]) == int:
            val += stack.pop()
        stack.append(val)
if len(stack) == 1 and type(stack[0]) == int:
    print(stack[0])
else:
    print('0')
