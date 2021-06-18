def solution(nums):
    def check(num):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True
        else:
            return False
    count, n = 0, len(nums)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if check(nums[i] + nums[j] + nums[k]):
                    count += 1
    return count

a = [1,2,3,4]
print(solution(a))