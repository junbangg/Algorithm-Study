def solution(people, limit):
    boat = []
    answer = 0
    people = sorted(people)
    while people:
        boat.append(people.pop())
        while people and sum(boat) + people[0] <= limit:
            boat.append(people.pop(0))
        answer += 1
        boat = []
    return answer

# or

def solution(people, limit):
    boat = []
    answer = 0
    people = sorted(people)
    while people:
        if not boat:
            boat.append(people.pop())
        elif people and sum(boat) + people[0] <= limit:
            boat.append(people.pop(0))
        else:
            answer += 1
            boat = []
    return answer + 1

# or

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
