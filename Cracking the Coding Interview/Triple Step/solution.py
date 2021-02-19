# pg. 134 - 8.1
def solution(n):
    def steps(x, y, z, total):
        if total > n:
            return
        elif total == n:
            results.append([x-1, y-1, z-1])
            return
        for i in range(x, n):
            for j in range(y, n):
                for k in range(z, n):
                    steps(i + 1, j + 1, k + 1, i + 2*j + 3*k)
    results = []
    steps(0, 0, 0, 0)
    return len(results) + 1

print(solution(5))

