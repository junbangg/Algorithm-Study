def solution(n, t, m, timetable):
    # 전처리
    q = []
    # q = [timestamp -> converted to minutes]
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
