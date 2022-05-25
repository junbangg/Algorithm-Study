import Foundation

func bfs(_ start: Int, _ destination: Int, _ paths: [Int: [Int]]) -> Bool {
    var visited = Array(repeating: false, count: paths.count)
    var q: [Int] = []
    var pointer = 0

    visited[start] = true
    q.append(start)

    while pointer < q.count {
        let currentNode = q[pointer]

        for nextNode in paths[currentNode]! {
            if visited[nextNode] {
                continue
            }
            if nextNode == destination {
                return true
            }
            visited[nextNode] = true
            q.append(nextNode)
        }

        pointer += 1
    }
    return false
}

let N = Int(readLine()!)!
let M = Int(readLine()!)!

var paths: [Int: [Int]] = [:]

for i in 0..<N {
    let data = readLine()!.split(separator: " ").compactMap { Int($0) }

    for (j, isPath) in data.enumerated() {
        if isPath == 1 {
            if paths[i] != nil {
                paths[i]!.append(j)
            } else {
                paths[i] = [j]
            }
        }
    }
}
let travelPath = readLine()!.split(separator: " ").compactMap { Int($0)! - 1 }

for i in 1..<travelPath.count {
    let start = travelPath[i-1]
    let destination = travelPath[i]
    
    if !bfs(start, destination, paths) {
        print("NO")
        exit(0)
    }
}
print("YES")
// 5
// 5
// 0 1 0 1 1
// 1 0 1 1 0
// 0 1 0 0 0 
// 1 1 0 0 0 
// 1 0 0 0 0
// 4 2 1 2 3