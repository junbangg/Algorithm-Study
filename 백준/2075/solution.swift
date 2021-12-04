let N = Int(readLine()!)!
var arr: [[Int]] = []

for _ in 0..<N {
    arr.append(readLine()!.split(separator: " ").compactMap { Int($0) })
}

var singleArr: [Int] = []
for x in 0..<N {
    for y in 0..<N {
        singleArr.append(arr[x][y])
    }
}

print(singleArr.sorted().reversed()[N-1])