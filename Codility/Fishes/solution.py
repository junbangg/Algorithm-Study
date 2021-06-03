#O(n)
def solution(A, B):
    if len(A) == 1:
        return 1
    answer, stack = 0, []
    for i in range(len(A)):
        a, b = A[i], B[i]
        if b == 0:
            survived = a
            if stack:
                while stack:
                    opponent = stack.pop()
                    if opponent > survived:
                        survived = opponent
                        stack.append(opponent)
                        break
                if survived == a:
                    answer += 1
            else:
                answer += 1
        if b == 1:
            stack.append(a)
    return answer + len(stack)

A = [4,3,2,5,1,6]
B = [0,1,0,1,0,0]
#
#A = [4,3,2,1,5]
#B = [0,1,0,0,0]
#A = [5,3,2,1,4,3,3]
#B = [1,0,0,0,0,0,0]
print(solution(A,B))



