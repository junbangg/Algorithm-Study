N = int(input())

def createCombinations(length, arr):
    if len(arr) == length:
        operators_list.append(arr[:])
        return
    arr.append(' ')
    createCombinations(length, arr)
    arr.pop()

    arr.append('+')
    createCombinations(length, arr)
    arr.pop()

    arr.append('-')
    createCombinations(length, arr)
    arr.pop()


for _ in range(N):
    operators_list = []
    n = int(input())
    createCombinations(n-1, [])
    nums = [str(i) for i in range(1, n+1)]
    for operators in operators_list:
        string = ''
        for i in range(n-1):
            string += nums[i] + operators[i]
        string += nums[-1]
        if eval(string.replace(' ', '')) == 0:
            print(string)
    print()


