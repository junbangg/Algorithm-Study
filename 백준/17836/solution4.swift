import Foundation

func getTime(_ x: Int, _ y: Int, _ nx: Int, _ ny: Int) -> Int {
    return abs(nx - x) + abs(ny - y)
}

func solution(_ N: Int, _ M: Int, _ T: Int, _ board: [[Int]]) -> Int {
    let dx = [1, -1, 0, 0]
    let dy = [0, 0, -1, 1]
    var visited = Array(repeating: Array(repeating: false, count: M), count: N)
    var q: [(Int, Int, Int)] = [(0, 0, 0)]
    var swordTime = Int.max
    var swordlessTime = Int.max
    var counter = 0
    visited[0][0] = true

    while counter < q.count {
        let (x, y, currentTime) = q[counter]

        for i in 0..<4 {
            let nx = x + dx[i]
            let ny = y + dy[i]

            if 0 > nx || N <= nx || 0 > ny || M <= ny || visited[nx][ny] || board[nx][ny] == 1 {
                continue
            }
            if nx == N-1 && ny == M-1 {
                swordlessTime = min(swordlessTime, currentTime + 1)
                break
            }
            if board[nx][ny] == 2 {
                swordTime = currentTime + 1 + getTime(nx, ny, N-1, M-1)
            }
            visited[nx][ny] = true
            q.append((nx, ny, currentTime+1))
        }
        counter += 1
    }
    return min(swordlessTime, swordTime)
}

let NMT = readLine()!.split(separator: " ").compactMap { Int($0) }
let N = NMT[0]
let M = NMT[1]
let T = NMT[2]
var board: [[Int]] = []

for _ in 0..<N {
    let col = readLine()!.split(separator: " ").compactMap { Int($0) }

    board.append(col)
}

let time = solution(N, M, T, board)

print(time <= T ? time : "Fail")
