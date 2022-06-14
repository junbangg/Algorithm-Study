from collections import Counter
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        answers = []
        def dfs(index, sentence):
            if index == len(s):
                answers.append(' '.join(sentence))
                return
            for i in range(index, len(s)):
                word = s[index:i+1]
                if words[word] == 0:
                    continue
                sentence.append(word)
                dfs(i+1, sentence)
                sentence.pop()
        
        words = Counter(wordDict)
        dfs(0, [])
        
        return answers
        
