import Foundation

let NMR = readLine()!.split(separator: " ").compactMap { Int($0) }
let N = NMR[0]
let M = NMR[1]
let R = NMR[2]
var arr: [[String]] = []

for _ in 0..<N {
    let temp = readLine()!.split(separator: " ").compactMap {String($0)}
    arr.append(String(temp))
}

let depth = min(N, M) / 2
for _ in 0..<R {
    for d in 0..<depth {
        let cache = arr[d][d]
        // top
        for col in (1+d)..<(M-d) {
            arr[d][col-1] = arr[d][col]
        }
        // right
        for row in (1+d)..<(N-d) {
            arr[row-1][M-1-d] = arr[row][M-1-d]
        }
        // bottom
        for col in stride(from: M-1-d, to: d, by: -1) {
            arr[N-1-d][col] = arr[N-1-d][col-1]
        }
        // left
        for row in stride(from: N-1-d, to: 1+d, by: -1) {
            arr[row][d] = arr[row-1][d]
        }
        arr[d+1][d] = cache
    }
}

for i in 0..<N {
    let temp = arr[i].joined(separator: " ")
    print(temp)
}
