def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(c_sum, index, comb):
            if c_sum == 0:
                answers.append(comb)
                return
            if c_sum < 0:
                return
            for i in range(index, len(candidates)):
                dfs(c_sum-candidates[i], i, comb+[candidates[i]])
        answers = []
        dfs(target, 0, [])
        return answers
