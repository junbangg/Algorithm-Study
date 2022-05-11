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
        
    return sorted(candidates, key = lambda person: (len(person_rooms[person]), closestToRoom(person, person_rooms, target), person))

target = 403
rooms = ["[403]James", "[404]Azad,Louis,Andy,andy,louis,A,B", "[101]Azad,Guard"]

print(solution(rooms, target))