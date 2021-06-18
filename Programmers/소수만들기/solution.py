from itertools import combinations 
def solution(nums):
    def check(num):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True
        else:
            return False
    nums = [i for i in combinations(nums, 3) if check(sum(i))]
    return len(nums)

a = [1,2,3,4]
print(solution(a))
