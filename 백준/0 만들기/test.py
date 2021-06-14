def solve(exp, cands):
    global answers
    if not cands:
        if not exp[-1].isnumeric():
            exp = exp[:-1]
        woSpaces = exp.replace(' ', '')
        if eval(woSpaces) == 0:
            answers.add(exp)
        return
    for op in ['+', '-', ' ']:
        solve(exp + cands[0] + op, cands[1:])
answers = set()
#c = ['1', '2', '3']
c = ['1', '2', '3', '4', '5', '6', '7']
solve('', c)
print(answers)