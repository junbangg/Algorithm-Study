from itertools import combinations
def solution(relation):
    answer = 0
    relation = list(map(list,zip(*relation)))
    rows = [i for i in range(len(relation))]
    candidates, combs = [], []

    for i in range(1, len(relation) + 1):
        for comb in list(combinations(rows, i)):
            combs.append(comb)
    for comb in combs:
        check = []
        # 최소성 체크
        cont = False
        for cand in candidates:
            for c in comb:
                if c in cand:
                    cont = True
                    break
        if cont:
            continue

        # 유일성 체크
        for col in range(len(relation[0])):
            tup = ()
            for row in comb:
                tup += (relation[row][col], )
            check.append(tup)
        if len(check) == len(set(check)):
            candidates.append(comb)
            answer += 1
    return answer

