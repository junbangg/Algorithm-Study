import sys
input = sys.stdin.readline
N = int(input())
cards = [0] + list(map(int, input().split()))
dp = [0] * (N+1)
dp[1] = cards[1]
dp[2] = max(cards[2], cards[1] * 2)
for i in range(3, N+1):
    dp[i] = cards[i]
    # 약수들
    for j in range(1, i//2 + 1):
        dp[i] = max(dp[i], dp[j] + dp[i-j])
print(dp[N])


def solution(n, t, m, timetable):
    # convert to minutes
    q = []
    for time in timetable:
        s = time.split(':')
        hour, minute = int(s[0]), int(s[1])
        total = hour*60 + minute
        q.append(total)
    # sort
    q.sort(reverse = True)
    # calculate
    i, cnt = 0, 0
    start, last = 540, 0
    while i < n and cnt < m:
        while q and q[-1] <= start + t*i:
            last = q.pop()
            cnt += 1
        i += 1
    # edge cases
    if cnt < m:
        edgeTime = 540 + (n-1) * t
        edgeHrs = str(edgeTime // 60)
        edgeMins = str(edgeTime % 60)
        if len(edgeHrs) == 1:
            edgeHrs = '0' + edgeHrs
        if len(edgeMins) == 1:
            edgeMins = '0' + edgeMins
        return edgeHrs + ':' + edgeMins
    # result
    latest = last - 1
    hr = str(latest // 60)
    mins = str(latest % 60)
    if len(mins) == 1:
        mins = '0' + mins
    if len(hr) == 1:
        hr = '0' + hr
    return hr + ':' + mins


    def solution(n, t, m, timetable):
    # convert to minutes
    q = []
    for time in timetable:
        s = time.split(':')
        hour, minute = int(s[0]), int(s[1])
        total = hour*60 + minute
        q.append(total)
    # sort
    q.sort(reverse = True)
    # calculate
    start, last = 540, 0
    for _ in range(n):
        for _ in range(m):
            if q and q[-1] <= start:
                last = q.pop() - 1
            else:
                last = start
        start += t
    # result 
    hr = str(last // 60)
    mins = str(last % 60)
    if len(mins) == 1:
        mins = '0' + mins
    if len(hr) == 1:
        hr = '0' + hr
    return hr + ':' + mins