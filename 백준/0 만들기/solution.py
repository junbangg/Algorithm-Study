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
N = int(input())
for _ in range(N):
    n = int(input())
    nums = list(map(str, [i for i in range(1, n+1)]))
    answers = set()
    solve('', nums)
    for a in answers:
        print(a)
    print()
