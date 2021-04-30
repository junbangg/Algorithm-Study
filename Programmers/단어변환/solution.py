from collections import Counter
def solution(begin, target, words):
    if target not in words:
        return 0
    answer = []
    def checkDiff(word1, word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
            if count >= 2:
                return False
        return True 
    def dfs(word, choices, count):
        if word == target:
            answer.append(count)
            return
        elif not choices:
            return
        for choice in choices:
            if checkDiff(choice, word):
                nextChoices = choices[:]
                nextChoices.remove(choice)
                next = choice
                dfs(next, nextChoices, count+1)
         
    dfs(begin, words, 0)
    return 0 if not answer else min(answer)
