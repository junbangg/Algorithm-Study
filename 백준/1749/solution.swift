import Foundation

func createPrefixSum(_ board: inout [[Int]]) {
    let N = board.count
    let M = board[0].count

    for x in 1..<N {
        for y in 1..<M {
            board[x][y] += board[x][y-1] + board[x-1][y] - board[x-1][y-1]
        }
    }
}

func getTotal(of board: [[Int]], _ x1: Int, _ y1: Int, _ x2: Int, _ y2: Int) -> Int {
    if x1 == x2 && y1 == y2 {
        return board[x2][y2] - board[x2-1][y2] - board[x2][y2-1] + board[x2-1][y2-1]
    }
    let left = board[x2][y1-1]
    let right = board[x1-1][y2]
    let mid = board[x1-1][y1-1]

    return board[x2][y2] - left - right + mid
}

func solution(_ board: [[Int]]) -> Int {
    let N = board.count
    let M = board[0].count
    var answer = -Int.max

    for x1 in 1..<N {
        for y1 in 1..<M {
            for x2 in x1..<N {
                for y2 in y1..<M {
                    answer = max(answer, getTotal(of: board, x1, y1, x2, y2))
                }
            }
        }
    }

    return answer
}

let NM = readLine()!.split(separator: " ").compactMap { Int($0) }
let N = NM[0]
let M = NM[1]

var board: [[Int]] = [Array(repeating: 0, count: M+1)]

for _ in 0..<N {
    let input = readLine()!.split(separator: " ").compactMap { Int($0) }

    board.append([0] + input)
}

createPrefixSum(&board)

print(solution(board))

