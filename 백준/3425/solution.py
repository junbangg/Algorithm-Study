# commands
cmds = []
while 1:
    data = input()
    if data == '':
        cmds = []
        continue
    elif data[0].isalpha():
        if data == 'QUIT':
            break
        cmds.append(data)
    elif data.isnumeric():
        # integers
        N = int(data)
        for _ in range(N):
            stack = [int(input())]
            for cmd in cmds:
                if cmd[0] == 'N':
                    _, x = cmd.split()
                    stack.append(int(x))
                elif cmd == 'POP':
                    if stack:
                        stack.pop()
                elif cmd == 'INV':
                    if stack:
                        a = stack.pop()
                        stack.append(-a)
                elif cmd == 'SWP':
                    if len(stack) > 1:
                        a = stack.pop()
                        b = stack.pop()
                        stack.append(b)
                        stack.append(a)
                elif cmd == 'ADD':
                    temp = 0
                    if len(stack) > 1:
                        a = stack.pop()
                        b = stack.pop()
                        stack.append(a+b)
                elif cmd == 'SUB':
                    if len(stack) > 1:
                        a = stack.pop()
                        b = stack.pop()
                        stack.append(a-b)
                elif cmd == 'MUL':
                    if len(stack) > 1:
                        a = stack.pop()
                        b = stack.pop()
                        stack.append(a*b)
                elif cmd == 'DIV':
                    if len(stack) > 1:
                        a = stack.pop()
                        b = stack.pop()
                        if abs(a) >= 1 and abs(b) >= 1:
                            stack.append(a//b)
                elif cmd == 'MOD':
                    if len(stack) > 1:
                        a = stack.pop()
                        b = stack.pop()
                        if abs(a) >= 1 and abs(b) >= 1:
                            temp = a%b
                            # if a < 0:
                            #     stack.append(-temp)
                            # else:
                            stack.append(temp) # check
                elif cmd == 'DUP':
                    if stack:
                        stack.append(stack[-1])

            if len(stack) > 1:
                print('ERROR')
            else:
                if stack and stack[0] <= 1000000000:
                    print(stack[0])
                else:
                    print('ERROR')
        print('\n')