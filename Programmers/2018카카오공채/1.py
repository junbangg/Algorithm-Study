import collections
def solution(lines):
    # convert log data -> tuple(start_sec, time_sec)
    logs = []
    for line in lines:
        logs.append(line.split()[1:])
    data = []
    for log in logs:
        time, sec = log[0].split(':'), log[1][:-1]
        seconds = 0
        seconds = int(time[0]) * 60 * 60 + int(time[1]) * 60 + float(time[2])
        data.append([float(str(float(seconds)-float(sec))+'1'), float(seconds)])
    answer = []
    left = int(min(data, key = lambda x: x[0])[0] * 1000)
    right = int(max(data, key = lambda x: x[1])[1] * 1000)
                # binary search




    



testCase = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

solution(testCase)

