def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    s1, s2 = [], []
    for i in range(1, len(str1)):
        sub = str1[i-1:i+1]
        if sub.isalpha():
            s1.append(sub)
    for i in range(1, len(str2)):
        sub = str2[i-1:i+1]
        if sub.isalpha():
            s2.append(sub)
    inter, union = 0, 0
    if set(s1) == set(s2):
        inter = min(len(s1), len(s2))
        union = max(len(s1), len(s2))
    else:
        inter = len(list(set(s1) & set(s2)))
        union = len(list(set(s1+s2)))
    div = 1
    if inter != 0 and union != 0:
        div = float(inter) / float(union)
    return int(div * 65536)



str1 = 'FRANCE'
str2 = 'french'
#str1 = 'handshake'
#str2 = 'shake hands'
print(solution(str1, str2))
