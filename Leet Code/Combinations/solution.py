class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        def dfs(nums, start, k):
            #base case
            if k == 0:
                results.append(nums[:])
            for i in range(start, n+1):
                nums.append(i)
                dfs(nums, i + 1, k - 1)
                nums.pop()

        dfs([], 1, k)
        return results

#or
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        def recurse(elements, start):
            if len(elements) == k:
                results.append(elements[:])
                return
            for i in range(start, n+1):
                elements.append(i)
                recurse(elements, i+1)
                elements.pop()
        recurse([], 1)
        return results
