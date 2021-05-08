from collections import defaultdict

def solution(v):
    answer = []
    x_dic = defaultdict(int)
    y_dic = defaultdict(int)
    for x, y in v:
        x_dic[x] += 1
        y_dic[y] += 1

    for x in x_dic:
        if x_dic[x] == 1:
            answer.append(x)
    for y in y_dic:
        if y_dic[y] == 1:
            answer.append(y)

    return answer


