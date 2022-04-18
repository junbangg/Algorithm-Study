def find(parents, a):
    if parents[a] != a:
        parents[a] = find(parents, parents[a])
    return parents[a]

def union(parents, a, b):
    aParent = find(parents, a)
    bParent = find(parents, b)
    if aParent < bParent:
        parents[aParent] = bParent
    else:
        parents[bParent] = aParent

def solution(k, room_number):
    rooms = [i for i in range(k+1)]
    answer = []
    for room in room_number:
        parent = find(rooms, room)
        answer.append(parent)
        if parent < k:
            union(rooms, parent, parent+1)
    return answer   
        