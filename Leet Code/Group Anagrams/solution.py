class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i, v in enumerate([''.join(sorted(c)) for c in strs]):
            if v not in dic:
                dic[v] = [strs[i]]
            else: dic[v].append(strs[i])
        return dic.values()
