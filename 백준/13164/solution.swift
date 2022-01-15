let NK = readLine()!.split(separator: " ").compactMap { Int($0) }
let N = NK[0]
let K = NK[1]

let array = readLine()!.split(separator: " ").compactMap { Int($0) }

var prefixArray: [Int] = []

for i in 1..<N {
    prefixArray.append(array[i] - array[i-1])
}

var answer = 0

prefixArray.sort()

print(prefixArray[0..<N-K].reduce(0, +))
