let NK = readLine()!.split(separator: " ").compactMap { Int($0) }
let N = NK[0]
let K = NK[1]

let numbers = readLine()!.split(separator: " ").compactMap { Int($0) }
var prefix: [Int] = [numbers[0]]

for i in 1..<numbers.count {
    prefix.append(prefix.last! + numbers[i])
}

var answer = 0

var counter: [Int: Int] = [:]

for i in 0..<prefix.count {
    if prefix[i] == K {
        answer += 1
    }
    if counter[prefix[i]-K] != nil {
        answer += counter[prefix[i] - K]!
    } else {
        counter[prefix[i]-K] = 0
    }
    if counter[prefix[i]] == nil {
        counter[prefix[i]] = 0
    } else {
        counter[prefix[i]]! += 1
    }
}

print(answer)