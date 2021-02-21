class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return itertools.permutations(nums, len(nums))

# or

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        prev_elements = []
        def dfs(elements):
            if len(elements) == 0:
                answer.append(prev_elements[:])
            for i in elements:
                temp = elements[:]
                temp.remove(i)

                prev_elements.append(i)
                dfs(temp)
                prev_elements.pop()
        dfs(nums)
        return answer
