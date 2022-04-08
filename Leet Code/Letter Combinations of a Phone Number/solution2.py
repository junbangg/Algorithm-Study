from re import L
from unicodedata import digit


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_letter = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        answer = []
        def dfs(index, path):
            if len(digits) == len(path):
                answer.append(path)
                return
            for i in range(len(digit_letter[digits[index]])):
                dfs(index+1, path + digit_letter[digits[index]][i])
        if not digits:
            return []
        dfs(0, "")
        return answer