import Foundation
// 끝내야하는 시간 기준으로 reverse sort
// 하나씩 tuple.1 - tuple.0
// 결과가 next의 tuple.1 보다 크면 그 차이만큼 max 로 저장
// 마지막 값에서 저장한 max 값 빼고, 0 보다 작으면 -1 리턴

func solution(_ data: [(Int, Int)]) -> Int {
    let data = data.sorted(by: {
        $0.1 > $1.1
    })
    let dataCount = data.count
    var requiredTime = 0
    var current = data[0].1

    for i in 1..<dataCount {
        current -= data[i-1].0
        if current > data[i].1 {
            requiredTime = max(requiredTime, current-data[i].1)
        }
    }
    current -= data[dataCount-1].0
    current -= requiredTime

    return current >= 0 ? current : -1
}


let N = Int(readLine()!)!
var data: [(Int, Int)] = []

for _ in 0..<N {
    let TS = readLine()!.split(separator: " ").compactMap { Int($0) }

    data.append((TS[0], TS[1]))
}

print(solution(data))

/** TC
6
1 1
1 2
1 3
1 4
1 5
1 6
-> 0
5
1 1
2 3
1 4
1 5
2 6
-> -1
4
3 5
8 15
5 20
2 16
-> 2
4
3 5
8 15
5 19
2 16
-> 1
4
3 5
8 15
5 17
2 16
*/
