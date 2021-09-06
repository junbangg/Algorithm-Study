import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    N = int(input())
    # 입력 숫자들 정렬
    nums = sorted([input().rstrip() for _ in range(N)])
    # 일관성이 계속 유지되는지 확인
    unique = True 
    for i in range(1, len(nums)):
        length = len(nums[i-1])
        if nums[i-1] in nums[i][:length]:
            unique = False
            break
    if unique:
        print('YES')
    else:
        print('NO')