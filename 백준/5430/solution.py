from collections import deque
tc = int(input())
for _ in range(tc):
    cmd = input()
    n = int(input())
    nums = input()
    if nums == '[]':
        nums = deque([])
    else:
        nums = deque((map(int, nums[1:-1].split(','))))
    error, front = False, True
    for c in cmd:
        if c == 'R':
            # toggle
            front = not front
        elif not nums:
            error = True
            print("error")
            break
        else:
            if front:
                nums.popleft()
            else:
                nums.pop()
    if not error:
        if not nums:
            print('[]')
        else:
            if not front:
                nums.reverse()
            output = '['
            for n in nums:
                output += str(n) + ','
            print(output[:-1] + ']')
            