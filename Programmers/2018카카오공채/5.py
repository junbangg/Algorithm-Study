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
    # edge cases
    allSmaller, allBigger = False, False 
    smallest, biggest = 540, 540 + (n-1) * t
    for time in q:
        if time < smallest:
            allSmaller = True 
        elif time > biggest:
            allBigger = True 
    if allSmaller:
        return '09:00'
    if allBigger:
        a = str(biggest//60)
        b = str(biggest%60)
        if len(a) == 1:
            a = '0' + a
        if len(b) == 1:
            b = '0' + b
        return a + ':' + b

    i, cnt = 0, 0
    start, last = 540, 0
    while i < n and cnt < m:
        while q and q[-1] <= start + t*i:
            last = q.pop()
            cnt += 1
        i += 1
    latest = last - 1
    hr = str(latest // 60)
    mins = str(latest % 60)
    if len(mins) == 1:
        mins = '0' + mins
    if len(hr) == 1:
        hr = '0' + hr
    return hr + ':' + mins

'''
n = 1
t = 1
m = 1
timetable = ["08:00", "08:01", "08:02", "08:03"]
#08:02
'''
'''
n = 2
t = 10
m = 2
timetable = ["09:10", "09:09", "08:00"]
#09:09
'''
'''
n = 2
t = 1
m = 2
timetable = ["09:00", "09:00", "09:00", "09:00"]
#08:59
'''
'''
n = 1
t = 1
m = 5
timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
#00:00
'''
n = 1
t = 1
m = 1
timetable = ["23:59"]
'''
n = 10
t = 60
m = 45
timetable = ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
'''
print(solution(n, t, m, timetable))
