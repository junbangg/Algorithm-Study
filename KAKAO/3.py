import heapq
def solution1(n, k, cmd):
    # result
    result = ['O'] * n
    # delete stack
    stack = []
    # heap
    minh, maxh = [], []
    # chart
    chart = [i for i in range(0, n)]
    # convert cmd to lists 
    for i in range(len(cmd)):
        cmd[i] = cmd[i].split()

    for order in cmd:
        c, x = '', 0
        if len(order) == 1:
            c = order[0]
        else:
            c, x = order[0], int(order[1])
        # start commands
        if c == 'U':
            if k - x <= 0:
                k = 0
            else:
                k = k - x
            #might have to figure out what happens when x cant go anywhere
            if chart[k] == -1:
                minItem = heapq.heappop(minh)
                k = minItem[1][0]
                heapq.heappush(minh, minItem)
        elif c == 'D':
            if k + x >= len(chart) - 1:
                k = len(chart) - 1
            else:
                k = k + x
            if chart[k] == -1:
                maxItem = heapq.heappop(maxh)
                k = maxItem[1][1]
                heapq.heappush(maxh, maxItem)
        elif c == 'C':
            result[k] = 'X'
            stack.append(k)
            chart[k] = -1
            left, right = 0, 0
            if not minh and not maxh:
                left, right = k-1, k+1
            else:
                minItem = heapq.heappop(minh)
                maxItem = heapq.heappop(maxh)
                left, right = minItem[1][0], maxItem[1][1]
                heapq.heappush(minh, minItem)
                heapq.heappush(maxh, maxItem)
                if left == k:
                    left = k - 1
                if right == k:
                    right = k + 1
            heapq.heappush(minh, [k, [left, right]])
            heapq.heappush(maxh, [-k, [left, right]])
            # next k position
            # if cant go down
            if k + 1 >= len(chart) - 1:
                # go up 
                if chart[k-1] == -1:
                    minItem = heapq.heappop(minh)
                    k = minItem[1][0]
                    heapq.heappush(minh, minItem)
            # can go down but is deleted
            elif chart[k + 1] == -1:
                maxItem = heapq.heappop(maxh)
                k = maxItem[1][1]
                heapq.heappush(maxh, maxItem)
            # can go down
            else:
                k -= 1
        # Z
        elif c == 'Z' and stack:
            last = stack.pop()
            result[last] = 'O'
            chart[last] = last
            minhDelete, maxhDelete = 0, 0
            for i in range(len(minh)):
                if minh[i][0] == last:
                    minhDelete = i
            for i in range(len(maxh)):
                if maxh[i][0] == last:
                    maxhDelete = i
            minh.pop(minhDelete)
            maxh.pop(maxhDelete)
    return ''.join(result)
import heapq
def solution(n, k, cmd):
    # result
    result = ['O'] * n
    # delete stack
    stack = []
    dic = {}
    for i in range(n):
        dic[i] = i
    # chart
    chart = [i for i in range(0, n)]
    # convert cmd to lists 
    for i in range(len(cmd)):
        cmd[i] = cmd[i].split()

    for order in cmd:
        c, x = '', 0
        if len(order) == 1:
            c = order[0]
        else:
            c, x = order[0], int(order[1])
        # start commands
        if c == 'U':
            if k - x <= 0:
                k = 0
            else:
                k = k - x
        elif c == 'D':
            if k + x >= len(chart) - 1:
                k = len(chart) - 1
            else:
                k = k + x
        elif c == 'C':
            result[dic[k]] = 'X'
            stack.append(k)
            chart.pop(k)
            # next k position
            # if cant go down
            '''
            if k + 1 >= len(chart) - 1:
                # go up 
                k -= 1
            # can go down
            else:
                k += 1
            '''
        # Z
        elif c == 'Z' and stack:
            last = stack.pop()
            result[dic[last]] = 'O'
            chart.insert(last, last)
        print(k)
        print(order)
        print(chart)
        print(stack)
    return ''.join(result)

n = 8 
k = 2 
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n, k, cmd))
