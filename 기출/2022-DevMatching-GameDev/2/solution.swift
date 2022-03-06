// Dev-Matching 2번 문제

import Foundation

func isValid(x: Int, y: Int, xLimit: Int, yLimit: Int) -> Bool {
    return x >= 0 && x < xLimit && y >= 0 && y < yLimit
}

func navigate(board: [[String]], x: Int, y: Int, directionX: Int, directionY: Int, visited: [[Bool]]) -> Int {
    let originalValue = board[x][y]
    var answer = 0
    var nx = x + directionX
    var ny = y + directionY
    
    while isValid(x: nx, y: ny, xLimit: board.count, yLimit: board[0].count) &&
            !visited[nx][ny] &&
            board[nx][ny] == originalValue {
        nx += directionX
        ny += directionY
        answer += 1
    }

    return answer
}

func calculateBidirection(
    direction1: String,
    direction2: String,
    board: [[String]],
    x: Int,
    y: Int,
    directionMap: [String: (Int, Int)],
    n: Int,
    visited: [[Bool]]
) -> Int {
    var answer = 0
    let (dx, dy) = directionMap[direction1]!
    let (dx2, dy2) = directionMap[direction2]!
    
    answer += navigate(board: board, x: x, y: y, directionX: dx, directionY: dy, visited: visited)
    answer += navigate(board: board, x: x, y: y, directionX: dx2, directionY: dy2, visited: visited)
    
    return answer
}



func solution(_ h:Int, _ w:Int, _ n:Int, _ board:[String]) -> Int {
    let board = board.map { $0.map { String($0) } }
    var answer = 0
    let directionMap = [
        "N": (-1, 0),
        "NE": (-1, 1),
        "E": (0, 1),
        "SE": (1, 1),
        "S": (1, 0),
        "SW": (1, -1),
        "W": (0, -1),
        "NW": (-1, -1)
    ]
//    var visited: [[[Bool]]] = Array(repeating: Array(repeating: Array(repeating: false, count: 9), count: w), count: h)
    var visited: [[Bool]] = Array(repeating: Array(repeating: false, count: w), count: h)
    
    for x in 0..<h {
        for y in 0..<w {
            if board[x][y] != "0" {
                // W, E
                if calculateBidirection(
                    direction1: "W",
                    direction2: "E",
                    board: board,
                    x: x,
                    y: y,
                    directionMap: directionMap,
                    n: n,
                    visited: visited
                ) == n - 1 {
                    answer += 1
                    visited[x][y] = true
                }
                // N, S
                if calculateBidirection(
                    direction1: "N",
                    direction2: "S",
                    board: board,
                    x: x,
                    y: y,
                    directionMap: directionMap,
                    n: n,
                    visited: visited
                ) == n - 1 {
                    answer += 1
                    visited[x][y] = true
                }
                // NW, SE
                if calculateBidirection(
                    direction1: "NW",
                    direction2: "SE",
                    board: board,
                    x: x,
                    y: y,
                    directionMap: directionMap,
                    n: n,
                    visited: visited
                ) == n - 1 {
                    answer += 1
                    visited[x][y] = true
                }
                // NE, SW
                if calculateBidirection(
                    direction1: "NE",
                    direction2: "SW",
                    board: board,
                    x: x,
                    y: y,
                    directionMap: directionMap,
                    n: n,
                    visited: visited
                ) == n - 1 {
                    answer += 1
                    visited[x][y] = true
                }
            }
        }
    }
    
    
    return answer
}
/**
 1 1 1 1 0 0 0 0 0
 0 0 0 0 1 0 0 1 1
 1 1 1 1 0 0 0 1 1
 1 1 1 1 1 0 0 1 1
 1 1 1 1 0 0 0 1 1
 1 1 1 1 0 0 0 1 0
 1 1 1 1 0 0 0 0 0
 
 1 1 1 1 1
 1 1 1 1 1
 1 1 1 1 1
 1 1 1 1 1
 1 1 1 1 1
 */
/// (W, E), (N, S), (NW, SE), (NE, SW)


//let h = 7, w = 9, n = 4
//let board = ["111100000","000010011","111100011","111110011","111100011","111100010","111100000"]

let h = 5, w = 5, n = 5
let board = ["11111","11111","11111","11111","11111"]

solution(h, w, n, board)

