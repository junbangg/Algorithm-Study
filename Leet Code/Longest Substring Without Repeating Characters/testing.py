a = ["abcdafg"]
stack = ["a", "b", "c", "d"]
if "b" in stack:
    index = stack.index("b")
    stack = stack[index+1:]
    print(stack)

