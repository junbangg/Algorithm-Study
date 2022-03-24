def convertToSeconds(log):
    data = log.split(':')
    return int(data[0]) * 60 * 60 + int(data[1]) * 60 + int(data[2])

def convertToLog(seconds):
    hours, seconds = divmod(seconds, 60*60)
    minutes, seconds = divmod(seconds, 60)

    hourString = str(hours)
    if hours < 10:
        hourString = '0' + hourString
    minutesString = str(minutes)
    if minutes < 10:
        minutesString = '0' + minutesString
    secondsString = str(seconds)
    if seconds < 10:
        secondsString = '0' + secondsString
    
    return hourString + ':' + minutesString + ':' + secondsString

def solution(play_time, adv_time, logs):
    playTimeSec = convertToSeconds(play_time)
    advTimeSec = convertToSeconds(adv_time)

    # step 2
    totalTime = [0 for _ in range(playTimeSec+1)]

    # step 1
    for log in logs:
        data = log.split('-')
        totalTime[convertToSeconds(data[0])] += 1
        totalTime[convertToSeconds(data[1])] -= 1

    # step 3
    for i in range(1, len(totalTime)):
        totalTime[i] = totalTime[i] + totalTime[i-1]
    
    # step 4
    for i in range(1, len(totalTime)):
        totalTime[i] = totalTime[i] + totalTime[i-1]

    maxTime = maxView = 0

    for i in range(advTimeSec - 1, playTimeSec):
        if i >= advTimeSec:
            if maxView < totalTime[i] - totalTime[i-advTimeSec]:
                maxView = totalTime[i] - totalTime[i - advTimeSec]
                maxTime = i - advTimeSec + 1
        else:
            if maxView < totalTime[i]:
                maxView = totalTime[i]
                maxTime = i - advTimeSec + 1

    return convertToLog(maxTime)