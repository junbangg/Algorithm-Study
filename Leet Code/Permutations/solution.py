class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return itertools.permutations(nums, len(nums))

# or
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        perms = []
        def dfs(elements, perms):
            if len(elements) == 0:
                results.append(perms[:])
                return
            for e in elements:
                perms.append(e)
                next = elements[:]
                next.remove(e)
                dfs(next, perms)
                perms.pop()
        dfs(nums, perms)
        return results
