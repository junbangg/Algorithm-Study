sk = "CBDK"
tree = ["CB", "CXYB", "BD", "AECD", "ABC", "AEX", "CDB", "CBKD", "IJCB", "LMDK"]
def solution(skill, skill_trees):
    answer = 0
    dic = {}
    first = skill[0]
    for i in range(1, len(skill)):
        dic[skill[i]] = skill[i-1]
    for s in skill_trees:
        st = []
        for c in s:
            if c in skill:
                st.append(c)
        if st and st[0] == first:
            if len(st) == 1:
                print(s)
                answer += 1
                break
            else:
                flag = True
                for j in range(1, len(st)):
                    if dic[st[j]] != st[j-1]:
                        flag = False
                        break
                if flag:
                    answer += 1
                    print(s)
    return answer
# answer
def solution(skill, skill_trees):
    ans = 0
    poss = []
    temp = ""
    for c in skill:
        temp += c
        poss.append(temp)
    for s in skill_trees:
        st = []
        for c in s:
            if c in skill:
                st.append(c)
        if not st or ''.join(st) in poss: ans += 1
    return ans
