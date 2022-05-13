import Foundation

func simulate() -> Bool {
    for start in 0..<N { // 1번 부터 N번 세로선까지 심사
        var current = start // 이동하는 가로선
        
        for j in 0..<H { // 가로선(행) 이동
            if board[j][current] { // 가로선 존재
                current += 1 // 가로선 이동
            } else if current > 0 && board[j][current-1] { // 가로선이 왼쪽에 존재하면
                current -= 1 // 가로선 왼쪽으로 이동
            }
        }
        if current != start {
            return false
        }
    }
    return true
}

func dfs(count: Int, x: Int, y: Int) {
    if simulate() {
        answer = min(count, answer)
        return
    } else if count == 3 || answer <= count { // 도착적이 정상적이지 않을때
        // count 값이 3일 경우 그 다음 호출에서 count가 4가 되어 문제 조건 위반하므로 return
        // count 값이 answer 보다 크거나 같으면 문제 조건에 의해서 -1 return
        return
    }
    // 행 이동
    for i in x..<H {
        let current = i == x ? y : 0

        // Fatal Range 오류 방지용 조건
        if current > N-1 {
            continue
        }
        for j in current..<N-1 {
            if !board[i][j] && !board[i][j+1] { // 가로선을 놨을떄 오른쪽에 - 가 존재하지않는 경우
                if j > 0 && board[i][j-1] {
                    continue
                }
                board[i][j] = true
                dfs(count: count + 1, x: i, y: j+2) // count 1 증가, 세로선 그대로, -- 이되면 안되므로 가로선은 2증가
                board[i][j] = false // 가로선 없애기
            }
        }
    }
}

let NMH = readLine()!.split(separator: " ").compactMap { Int($0) }
let N = NMH[0]
let M = NMH[1]
let H = NMH[2]

var board = Array(repeating: Array(repeating: false, count: N), count: H)

if M == 0 {
    print(0)
    exit(0)
}

for _ in 0..<M {
    let AB = readLine()!.split(separator: " ").compactMap { Int($0) }
    let A = AB[0]
    let B = AB[1]
    
    board[A-1][B-1] = true
}

var answer = 4
dfs(count: 0, x: 0, y: 0)
print(answer < 4 ? answer : -1)
