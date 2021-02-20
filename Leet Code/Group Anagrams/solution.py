class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        while strs:
            word = strs.pop()
            anagrams = [word]
            while strs:
                check = strs[len(strs)-1]
                if Counter(word) == Counter(check):
                    anagrams.append(check)
                    strs.pop()
            results.append(anagrams)
        return results
