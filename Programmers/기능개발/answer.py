import math
def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i]) / speeds[i]))
    cur = days[0]
    counter = 1
    for i in range(1, len(days)):
        if days[i] > cur:
            answer.append(counter)
            counter = 1
            cur = days[i]
        else:
            counter += 1
    answer.append(counter)
    return answer
