from collections import defaultdict

def closestToRoom(person, person_rooms, target):
    minDistance = float('inf')
    for room in person_rooms[person]:
        minDistance = min(minDistance, abs(target-room))
    
    return minDistance

def solution(rooms, target):
    person_rooms = defaultdict(list)
    uniquePeople = set()
    for data in rooms:
        roomRawString, peopleString = data.split(']')
        roomNumber = int(roomRawString[1:])
        people = peopleString.split(',')
        for person in people:
            person_rooms[person].append(roomNumber)
            uniquePeople.add(person)
    candidates = []
    for person in uniquePeople:
        if target in person_rooms[person]:
            continue
        candidates.append(person)
    print(person_rooms)
    print(candidates)
    for person in candidates:
        print(person)
        print(closestToRoom(person, person_rooms, target))
    return sorted(candidates, key = lambda k: (len(person_rooms[k]), closestToRoom(k, person_rooms, target), k))

target = 403
rooms = ["[403]James", "[404]Azad,Louis,Andy,andy,louis,A,B", "[101]Azad,Guard"]

print(solution(rooms, target))