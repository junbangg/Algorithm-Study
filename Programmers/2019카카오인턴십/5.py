def solution(k, room_number):
    answer = []
    vacant = [i for i in range(k)]
    occupied = [False] * k
    for num in room_number:
        if not occupied[num-1]:
            occupied[num-1] = True
            vacant.pop(num-1)
            answer.append(num)
        else:
            for v in vacant:
                if v > num:
                    occupied[v] = True
                    vacant.pop(v)
                    answer.append(num)
    return answer



