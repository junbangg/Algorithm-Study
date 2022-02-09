func isDividable(by number: Int, in numbers: [Int], M: Int) -> Bool {
    var _min = Int.max
    var _max = -Int.max
    var count = 1
    
    for i in 0..<numbers.count {
        _min = min(_min, numbers[i])
        _max = max(_max, numbers[i])
        if _max - _min > number {
            count += 1
            _max = numbers[i]
            _min = numbers[i]
        }
    }
    return count <= M
}

let NM = readLine()!.split(separator: " ").compactMap { Int($0) }
let N = NM[0]
let M = NM[1]
let numbers = readLine()!.split(separator: " ").compactMap { Int($0) }

var right = numbers.max()! - numbers.min()!
var left = 0

while left <= right {
    let mid = left + (right - left) / 2
    if isDividable(by: mid, in: numbers, M: M) {
        right = mid - 1
    } else {
        left = mid + 1
    }
}
print(left)
