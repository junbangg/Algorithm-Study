def solution(n):
    def recurse(n, count):
        if n == 0:
            return count
        if n % 2 == 0:
            return recurse(n//2, count)
        else:
            return recurse(n-1, count + 1)
    return recurse(n, 0)

print(solution(7))
    
