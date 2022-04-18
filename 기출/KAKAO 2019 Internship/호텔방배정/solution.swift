import Foundation

func find(_ rooms: inout [Int], _ number: Int) -> Int {
    if rooms[number] != number {
        rooms[number] = find(rooms, rooms[number])
    }
    return rooms[number]
}

func union(_ rooms: inout [Int], _ a: Int, _ b: Int) -> Int {
    let aParent = find(rooms, a)
    let bParent = find(rooms, b)
    if aParent <= bParent {
        rooms[bParent] = aParent
    } else {
        rooms[aParetn] = bParent
    }
}

func solution(_ k:Int64, _ room_number:[Int64]) -> [Int64] {
    var answer: [Int] = []
    var rooms = Array(0..<k+1)
    
    for room in room_number {
        let parent = find(rooms, room)
        answer.append(parent)
        if parent < k {
            union(rooms, parent, parent + 1)
        }
    }

    return answer

}