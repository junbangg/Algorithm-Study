public func solution(_ H : inout [Int]) -> Int {
    if H == [] {
        return 0
    }
    var stack = [Int]()
    var answer = 0
    for i in 0...H.count-1 {
        while stack.count != 0 && stack.last! > H[i] {
            stack.removeLast()
        }
        if stack.count == 0 || stack.last! < H[i] {
            stack.append(H[i])
            answer += 1
        }
    }
    return answer

