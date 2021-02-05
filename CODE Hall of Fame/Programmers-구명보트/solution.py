def solution(people, limit):
    people.sort()
    answer = 0
    light, heavy = 0, len(people) - 1
    while light <= heavy:
        answer += 1
        if people[heavy] + people[light] <= limit:
            light += 1
        heavy -= 1
    return answer
