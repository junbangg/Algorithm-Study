from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

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
    rooms = defaultdict(int)
    answer = []
    for room in room_number:
        parent = 0
        if rooms[room] == 0:
            rooms[room] = room
            answer.append(room)
            parent = room
        else:
            parent = find(rooms, room)
            answer.append(parent)
        if parent < k:
            if rooms[parent] == 0:
                rooms[parent] = parent
            if rooms[parent+1] == 0:
                rooms[parent+1] = parent+1
            union(rooms, parent, parent+1)
    return answer