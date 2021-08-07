import Foundation

// Input
let NM = readLine()!.split(separator: " ").compactMap{Int($0)}
let N = NM[0]
let M = NM[1]
var graph = [[Int]](repeating: [], count: N+1)
for _ in 0..<M {
    let AB = readLine()!.split(separator: " ").compactMap{ Int($0) }
    let A = AB[0]
    let B = AB[1]
    graph[B].append(A)
}
print(graph)

// BFS / DFS

// Solve