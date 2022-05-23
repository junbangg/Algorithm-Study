import Foundation

func countWater(_ x: Int, _ y: Int, _ board: [[Int]]) -> Int {
    let dx = [0, 0, 1, -1]
    let dy = [1, -1, 0, 0]
    var waterCount = 0
    var nx = x
    var ny = y

    for i in 0..<4 {
        nx = x + dx[i]
        ny = y + dy[i]

        if board[nx][ny] == 0 {
            waterCount += 1
        }
    }

    return waterCount
}

func melt(_ ice: [(Int, Int)], in board: inout [[Int]]) -> [(Int, Int)] {
    var newIce: [(Int, Int)] = []
    var iceToMelt: [(Int, Int, Int)] = [] // x, y, count

    for (x, y) in ice {
        let surroundingWaterCount = countWater(x, y, board)
        let meltingIceCount = min(board[x][y], surroundingWaterCount)

        iceToMelt.append((x, y, meltingIceCount))
    }

    for (x, y, count) in iceToMelt {
        board[x][y] -= count
        if board[x][y] > 0 {
            newIce.append((x, y))
        }
    }

    return newIce
}

func bfs(_ x: Int, _ y: Int, _ board: [[Int]], _ dx: [Int], _ dy: [Int], _ visited: inout [[Bool]]) {
    var q: [(Int, Int)] = []

    visited[x][y] = true
    q.append((x, y))

    var pointer = 0

    while pointer < q.count {
        let (x, y) = q[pointer]

        for i in 0..<4 {
            let nx = x + dx[i]
            let ny = y + dy[i]

            if nx < 0 || nx >= board.count || ny < 0 || ny >= board[0].count || visited[nx][ny] || board[nx][ny] == 0 {
                continue
            }
            visited[nx][ny] = true

            q.append((nx, ny))
        }

        pointer += 1
    }
}

func countGlaciers(_ ice: [(Int, Int)], _ board: [[Int]]) -> Int {
    let dx = [0, 0, 1, -1]
    let dy = [1, -1, 0, 0]
    var visited: [[Bool]] = Array(repeating: Array(repeating: false, count: board[0].count), count: board.count)
    var glacierCount = 0

    for (x, y) in ice {
        if visited[x][y] {
            continue
        }
        bfs(x, y, board, dx, dy, &visited)
        glacierCount += 1
    }

    return glacierCount
}

let NM = readLine()!.split(separator: " ").compactMap { Int($0) }
let N = NM[0]
let M = NM[1]

var board: [[Int]] = []

for _ in 0..<N {
    let row = readLine()!.split(separator: " ").compactMap { Int($0) }

    board.append(row)
}

var ice: [(Int, Int)] = []

for x in 0..<N {
    for y in 0..<M {
        if board[x][y] != 0 {
            ice.append((x, y))
        }
    }
}

var time = 0
let dx = [0, 0, 1, -1]
let dy = [1, -1, 0, 0]

while true {
    // apply and return new ice
    ice = melt(ice, in: &board)
    
    if ice.isEmpty {
        print(0)
        exit(0)
    }
    time += 1
    let glacierCount = countGlaciers(ice, board)
    if glacierCount >= 2 {
        break
    }
}

print(time)