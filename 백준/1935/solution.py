n = int(input())
exp = list(input())
# expression -> postorder
# convert Alphabet to ascii
for i, v in enumerate(exp):
    if v.isalpha():
        exp[i] = ord(v) % 65
# plug in number to list
nums = []
for _ in range(n):
    nums.append(int(input()))
for i, v in enumerate(exp):
    if type(v) == int:
        exp[i] = nums[v]

stack = []
# calculate postfix
for item in exp:
    # if num
    if type(item) == int:
        stack.append(item)
    # if operator
    else:
        a = stack.pop()
        b = stack.pop()
        c = 0
        if item == '+':
            c = float(b + a)
        if item == '-':
            c = float(b - a)
        if item == '/':
            c = b / a
        if item == '*':
            c = float(b * a)
        stack.append(c)
print("{0:.2f}".format(stack[0]))
