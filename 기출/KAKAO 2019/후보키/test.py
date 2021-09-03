from itertools import combinations
def solution(relation):
    answer = 0
    relation = list(map(list,zip(*relation)))
    rows = [i for i in range(len(relation))]
    candidates = []
    combs = []
    for i in range(1, len(relation) + 1):
        for comb in list(combinations(rows, i)):
            combs.append(comb)
        # combs.append(list(combinations(rows, i)))
    print(combs)
    for comb in combs:
        print('comb', comb)
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
        for col in range(len(relation[0])):
            tup = ()
            for row in comb:
                tup += (relation[row][col], )
            check.append(tup)
        print('check', check)
        if len(check) == len(set(check)):
            candidates.append(comb)
            answer += 1
            print('candidates', candidates)
    print(answer)
    return answer

# relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
relation = [["a", "1", "4"], 
["2", "1", "5"], 
["a", "2", "4"]]
# relation = [["100", "r"], 
# ["200", "c"], 
# ["300", "d"]]

print(solution(relation))