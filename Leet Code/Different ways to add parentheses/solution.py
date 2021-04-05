class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, op, right):
            result = []
            for l in left:
                for r in right:
                    result.append(eval(str(l) + op + str(r)))
            return result
        #base case
        answer = []
        if expression.isdigit():
            return [int(expression)]
        for index, val in enumerate(expression):
            if val in "-+*":
                a = self.diffWaysToCompute(expression[:index])
                b = self.diffWaysToCompute(expression[index+1:])
                answer.extend(compute(a, val, b))
        return answer
