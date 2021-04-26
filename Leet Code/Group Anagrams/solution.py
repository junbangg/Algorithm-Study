class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i, v in enumerate([''.join(sorted(c)) for c in strs]):
            if v not in dic:
                dic[v] = [strs[i]]
            else: dic[v].append(strs[i])
        return dic.values()


# or

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for word in strs:
            dic[''.join(sorted(word))].append(word)
        return dic.values()


# or
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #deep copy list
        str_copy = strs[:]
        #sort each element of list
        for i in range(len(str_copy)):
            temp = sorted(str_copy[i])
            str_copy[i] = ''.join(temp)
        #create default dict for indices
        dic = collections.defaultdict(list)
        for i, v in enumerate(str_copy):
            dic[v].append(i)
        # use indices to get original strings
        result = []
        for ind in dic.values():
            temp = []
            for i in ind:
                temp.append(strs[i])
            result.append(temp)
        return result

