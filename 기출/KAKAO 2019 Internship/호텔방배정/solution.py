def solution(k, room_number):
    dic = {}
    for num in range(1, k+1):
        dic[num] = num
    
    answer = []
    for number in room_number:
        answer.append(getVacantSpot(dic, number, k))
    return answer
    
def getVacantSpot(dic, number, k):
    if dic[number] == number:
        if number == 10:
            dic[number] = 1
        else:
            dic[number] += 1
        return number
    if number < k:
        return getVacantSpot(dic, number+1, k)
    else:
        return getVacantSpot(dic, 1, k)
k = 1
tc = [10]
print(solution(k, tc))