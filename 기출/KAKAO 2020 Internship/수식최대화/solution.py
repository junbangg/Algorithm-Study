from itertools import permutations

def calculate(expression, i, operators):
    if expression.isdigit():
        return str(expression)
    else:
        temp = []
        expression = expression.split(operators[i])
        for exp in expression:
            temp.append(calculate(exp, i+1, operators))
        return str(eval(operators[i].join(temp)))
            
def solution(expression):
    answer = 0
    operators = list(permutations(['*', '-', '+'], 3))
    for op in operators:
        answer = max(answer, abs(int(calculate(expression, 0, op))))
    return answer