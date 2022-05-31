import Foundation

/**
0 2 0
0 1 0
0 1 0
-> 4

0 0 0 1
0 1 0 0
2 1 1 0
0 1 0 0
0 1 0 1
0 0 0 0
-> 8
*/
func getTime(_ x: Int, _ y: Int, _ nx: Int, _ ny: Int) -> Int {
    return abs(nx - x) + abs(ny - y)
}

func solution(_ N: Int, _ M: Int, _ T: Int, _ board: [[Int]]) -> Int? {
    typealias Point = (x: Int, y: Int)
    let dx = [1, -1, 0, 0]
    let dy = [0, 0, -1, 1]
    var time = Array(repeating: Array(repeating: Int.max, count: M), count: N)
    var q: [Point] = [Point(0, 0)]
    var counter = 0

    time[0][0] = 0

    while counter < q.count {
        let current = q[counter]

        for i in 0..<4 {
            let nx = current.x + dx[i]
            let ny = current.y + dy[i]

            if 0 > nx || N <= nx || 0 > ny || M <= ny || board[nx][ny] == 1 {
                continue
            }
            var nextTime = time[current.x][current.y] + 1
            // 0 or 2
            if time[nx][ny] >= nextTime {
                time[nx][ny] = nextTime 
                q.append(Point(nx, ny))
            }
            if board[nx][ny] == 2 {
                nextTime += getTime(nx, ny, N-1, M-1)

                if time[N-1][M-1] >= nextTime {
                    time[N-1][M-1] = nextTime 
                }
            } 
        }
        counter += 1
    }
    return time[N-1][M-1] <= T ? time[N-1][M-1] : nil
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

guard let time = solution(N, M, T, board) else {
    print("FAIL")
    exit(0)
}

print(time)
