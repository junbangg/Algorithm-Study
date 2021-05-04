import collections
def solution(s):
    # prepare data
    s = s[1:-1]
    temp, tuples = "", []
    add = False
    for c in s:
        if c == '{':
            add = True
        elif c == '}':
            add = False
            tuples.append(temp)
            temp = ""
        elif add:
            temp += c
    tuples = [t.split(',') for t in tuples]
    # sort
    tuples.sort(key = len)
    # orderd dict
    od = collections.OrderedDict()
    for tup in tuples:
        for n in tup:
            od[n] = 1
    return list(map(int, od.keys()))

s = "{{20,111},{111}}"
print(solution(s))

