extension Int {
    var isEven: Bool {
        return self % 2 == 0
    }
    
    var isOdd: Bool {
        return self % 2 == 1
    }
}

let NK = readLine()!.split(separator: " ").compactMap { Int($0) }
let N = NK[0]
let K = NK[1]

let arr = readLine()!.split(separator: " ").compactMap { Int($0) }

var answer = 0
var left = 0
var right = 0
var evenCount = 0
var oddCount = 0

while right < N {
    if arr[right].isEven {
        evenCount += 1
    } else {
        oddCount += 1
    }
    if oddCount > K {
        answer = max(answer, evenCount)
        while arr[left].isEven {
            left += 1
            evenCount -= 1
        }
        left += 1
        oddCount -= 1
    }
    right += 1
}

if oddCount + evenCount == N {
    answer = evenCount
}

print(answer)

