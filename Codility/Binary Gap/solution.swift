public func solution(_ N : Int) -> Int {
    // write your code in Swift 4.2.1 (Linux)
    let str = String(N, radix: 2)
    var answer = 0
    var count = 0
    var startCount = false
    for c in str {
        if startCount && c == "0" {
            count += 1
        }
        if c == "1" {
            startCount = true
            if answer <= count {
                answer = count
            }
            count = 0
        }
    }
    return answer
}
