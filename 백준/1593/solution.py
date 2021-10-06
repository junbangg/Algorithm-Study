import sys, collections
input = sys.stdin.readline
w_len, s_len = map(int, input().split())
W = input().rstrip()
S = input().rstrip()

targetsLeft = len(set(W))
targetCnts = collections.Counter(W)
cnts = collections.defaultdict(int)
    
# S의 첫 4개 적용
for i in range(w_len):
    cnts[S[i]] += 1
    if targetCnts[S[i]] >= cnts[S[i]]:
        if cnts[S[i]] == targetCnts[S[i]]:
            targetsLeft -= 1

answer = 0
left, right = 0, w_len - 1
while right < s_len:
    if targetsLeft == 0:
        answer += 1

    if targetCnts[S[left]] >= cnts[S[left]]:
        if cnts[S[left]] == targetCnts[S[left]]:
            targetsLeft += 1
    cnts[S[left]] -= 1
    left += 1

    right += 1
    if right < s_len:
        cnts[S[right]] += 1
        if targetCnts[S[right]] >= cnts[S[right]]:
            if cnts[S[right]] == targetCnts[S[right]]:
                targetsLeft -= 1

print(answer)


# 4 10
# aabb
# ababacabba
# -> 3

# 3 10
# abc
# acbbacbcad
# -> 4

# 6 8
# aaabbb
# abababac
# -> 2

# 10 10
# abcdefghij
# abcdefghij
# -> 1


# 3 10
# aaa
# aaaaaaaaaa
# -> 8