let N = Int(readLine()!)!
let array = readLine()!.split(separator: " ").compactMap { Int($0) }

var arrowPosition = Array(repeating: 0, count: 1000001)
var answer = 0

for height in array {
    if arrowPosition[height] == 0 {
        answer += 1
    } else {
        arrowPosition[height] -= 1
    }
    arrowPosition[height - 1] += 1
}

print(answer)
