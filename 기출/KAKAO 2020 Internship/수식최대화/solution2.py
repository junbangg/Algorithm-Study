from itertools import permutations

def isSingleNumber(expression, operators):
    for op in operators:
        if op in expression:
            return False
    return True

def calculate(expression, i, operators):
    if expression.isdigit():
        return abs(int(str(expression)))
    else:
        temp = []
        expression = expression.split(operators[i])
        for exp in expression:
            temp.append(calculate(exp, i+1, operators))
        return abs(int(str(eval(operators[i].join(temp)))))

# def calculate(expression, operators, priorities, index):
#     if isSingleNumber(expression, operators):
#         return int(expression)
#     priority = priorities[index]
#     subExpressions = expression.split(operators[priority])
#     result = 0
#     newExpression = ''
#     for i, subExpression in enumerate(subExpressions):
#         if i == 0:
#             result = calculate(subExpression, operators, priorities, index+1)
#         else:
#             result = eval(str(result) + operators[priority] + str(calculate(subExpression, operators, priorities, index + 1)))
#     return abs(result)

def solution(expression):
    operators = ['-', '+', '*']
    answer = 0
    for priorities in permutations(range(3), 3):
        answer = max(answer, calculate(expression, operators, priorities, 0))

    return answer


operators = ['-', '+', '*']
# priorities = [2, 0, 1]
priorities = [0, 1, 2]
expression = "50*6-3*2"


# print(calculate(expression, operators, priorities, 0))
print(solution(expression))

