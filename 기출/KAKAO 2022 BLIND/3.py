
# if 누적 시간 <= 기본시간: 기본 요금
# if 누적 시간 > 기본시간:
    # 기본 요금 + math.ceil((누적 시간 - 기본 시간) / 단위 시간) * 단위 요금



import math
from collections import defaultdict
#fees
# 0: 기본 시간
# 1: 기본 요금
# 2: 단위 시간
# 3: 단위 요금

# records
# 시각 / 차량번호 / IN/OUT

def convert(time):
    hours, mins = time.split(':')
    return 60 * int(hours) + int(mins)

def solution(fees, records):

    car_time = defaultdict(list) # id: [total, last_data, state]
    car_time = {}
    
    lastTime = convert('23:59')

    for data in records:
        time, id, state = data.split()
        minutes = convert(time)
        if id in car_time:
            if state == 'IN':
                car_time[id][1] = minutes
            else:
                car_time[id][0] += (minutes - car_time[id][1])
                car_time[id][1] = 0
            car_time[id][2] = state
        else:
            car_time[id] = [0, minutes, state]
    for id in car_time:
        if car_time[id][2] == 'IN':
            car_time[id][0] += lastTime - car_time[id][1]
            car_time[id][1] = 0

    print(car_time)
    answer = []
    for id, data in car_time.items():
        fee = fees[1]
        if data[0] > fees[0]:
            fee += math.ceil((data[0] - fees[0]) / fees[2]) * fees[3]
        answer.append([id, fee])


    return [fee for _, fee in sorted(answer, key = lambda x: x[0])]


tc1 = [[180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]]
# tc2 = [[1, 461, 1, 10], ["00:00 1234 IN"]]
print(solution(tc1[0], tc1[1]))
