import Foundation

func printBoard(_ board: [[Int]]) {
    for i in 0..<board.count {
        print(board[i])
    }
}

func isMeltable(_ board: [[Int]], _ x: Int, _ y: Int, _ dx: [Int], _ dy: [Int]) -> Bool {
    var count = 0
    
    for i in 0..<4 {
        let nx = x + dx[i]
        let ny = y + dy[i]
        
        if board[nx][ny] == 0 {
            count += 1
        }
    }
    
    return count >= 2 ? true : false
}


func bfs(_ src_x: Int, _ src_y: Int, _ board: inout [[Int]]) -> Bool {
    let xLimit = board.count
    let yLimit = board[0].count
    let dx = [1, -1, 0, 0]
    let dy = [0, 0, 1, -1]
    var visited = Array(repeating: Array(repeating: false, count: yLimit), count: xLimit)
    var cheeseAirCount = Array(repeating: Array(repeating: 0, count: yLimit), count: xLimit)
    var q: [[Int]] = []
    var meltableCheese: [(Int, Int)] = []
    
    visited[src_x][src_y] = true
    q.append([src_x, src_y]) // x, y
    
    var counter = 0
    while counter < q.count {
        let data = q[counter]
        let x = data[0]
        let y = data[1]
        
        // 0, 0 check
        if counter == 0 && board[x][y] == 1 && isMeltable(board, x, y, dx, dy) {
            cheeseAirCount[x][y] += 1
        }
        
        for i in 0..<4 {
            let nx = x + dx[i]
            let ny = y + dy[i]
            
            if nx >= xLimit || nx < 0 || ny >= yLimit || ny < 0 || visited[nx][ny] {
                continue
            }
            
            // if cheeze and valid cheese
            if board[nx][ny] == 1 {
                cheeseAirCount[nx][ny] += 1
            } else {
                visited[nx][ny] = true
                q.append([nx, ny])
            }
        }
        counter += 1
    }
    var isMelted = false
    for x in 0..<xLimit {
        for y in 0..<yLimit {
            if cheeseAirCount[x][y] >= 2 {
                board[x][y] = 0
                isMelted = true
            }
        }
    }
//    for (x, y) in meltableCheese {
//        board[x][y] = 0
//    }
    printBoard(board)
    return isMelted
}

let NM = readLine()!.split(separator: " ").compactMap { Int($0) }
let N = NM[0]
let M = NM[1]

var board: [[Int]] = []
for _ in 0..<N {
    board.append(readLine()!.split(separator: " ").compactMap { Int($0) })
}

var time = 0
while true {
    if bfs(0, 0, &board) {
        time += 1
    } else {
        break
    }
}

print(time)

// 0 0 0 0 0 0 0 0 0
// 0 0 0 0 0 0 0 0 0
// 0 1 1 0 0 0 1 1 0
// 0 1 0 1 1 1 0 1 0
// 0 1 0 0 1 0 0 1 0
// 0 1 0 1 1 1 0 1 0
// 0 1 1 0 0 0 1 1 0
// 0 0 0 0 0 0 0 0 0
