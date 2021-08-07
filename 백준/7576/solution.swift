import Foundation

typealias Coord = (x: Int, y: Int)
//Solution
func solution(_ graph: [[Int]], _ M: Int, _ N: Int) -> Int {
    var graph = graph
    var q: [Coord] = []
    let dir: [Coord] = [(0,1), (0,-1), (1, 0), (-1,0)]
    var answer = 0
    /**
    First Traversal:
        1. If 1 : add Coord to queue
        2. If 0 : increment -> unripe
    **/
    var unripe = 0
    for i in 0..<N {
        for j in 0..<M {
            // 익은 토마토 큐에 적재
            if (graph[i][j] == 1) {
                q.append(Coord(i, j))
            } else if(graph[i][j] == 0) {
                unripe += 1
            }
        }
    }
    // 예외처리
    if unripe == 0 {
        return 0
    }
    // BFS
    var head = 0
    while head < q.count {
        let cur = q[head]
        for i in 0..<4 {
            let nx = cur.x + dir[i].x
            let ny = cur.y + dir[i].y
            if (0 <= nx && nx < N && 0 <= ny && ny < M && graph[nx][ny] == 0) {
                unripe -= 1
                graph[nx][ny] = graph[cur.x][cur.y] + 1
                answer = max(graph[nx][ny], answer)
                q.append((nx, ny))
            }
        }
        head += 1
    }
    if (unripe > 0) {
        return -1
    }
    return answer-1
}
//Input
let MN = readLine()!.split(separator: " ").compactMap{Int($0)}
let M = MN[0]
let N = MN[1]
var graph: [[Int]] = []
for _ in 0..<N {
    let nums = readLine()!.split(separator: " ").compactMap{Int($0)}
    graph.append(nums)
}
// Solve
print(solution(graph, M, N))