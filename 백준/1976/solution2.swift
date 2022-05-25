import Foundation

func find(_ parent: inout [Int], _ node: Int) -> Int {
    if parent[node] != node {
        parent[node] = find(&parent, parent[node])
    }
    return parent[node]
}

func union(_ parent: inout [Int], _ a: Int, _ b: Int) {
    let aParent = find(&parent, a)
    let bParent = find(&parent, b)

    if aParent < bParent {
        parent[bParent] = aParent
    } else {
        parent[aParent] = bParent
    }
}

let N = Int(readLine()!)!
let M = Int(readLine()!)!

var parent: [Int] = []

for i in 0..<N {
    parent.append(i)
}

for i in 0..<N {
    let data = readLine()!.split(separator: " ").compactMap { Int($0) }

    for (j, isPath) in data.enumerated() {
        if isPath == 1 {
            union(&parent, i, j)
        }
    }
}
let travelPath = readLine()!.split(separator: " ").compactMap { Int($0)! - 1 }

for i in 1..<travelPath.count {
    let start = travelPath[i-1]
    let destination = travelPath[i]
    
    if find(&parent, start) != find(&parent, destination) {
        print("NO")
        exit(0)
    }
}
print("YES")