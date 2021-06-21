from collections import defaultdict
def solution(n, words):
    dic = defaultdict(int)
    prev = words[0][0]
    turn = [0 for i in range(n)]
    for i, word in enumerate(words):
        num = (i % n) + 1
        turn[num - 1] += 1
        if dic[word] == 1 or prev != word[0]:
            return num, turn[num - 1]
        else:
            dic[word] = 1
            prev = word[-1]
    return [0, 0]
