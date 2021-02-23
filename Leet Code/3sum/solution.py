class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        cands = [sorted(c) for c in map(list, itertools.combinations(nums, 3)) if sum(c) == 0]
        return set(map(tuple, cands))

# better solution

