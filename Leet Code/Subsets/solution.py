class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, path):
            answers.append(path)
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])
        answers = []
        dfs(0, [])
        return answers
