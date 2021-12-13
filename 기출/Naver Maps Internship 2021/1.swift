
func calculateDigitSum(of n: Int) -> Int {
    var sum = 0
    var number = n
    while number != 0 {
        sum = sum + number % 10
        number = number / 10
    }
    return sum
}

public func solution(_ N : Int) -> Int {

    var number = 1
    var answer = 0
    while true {
        if calculateDigitSum(of: number) == N {
            answer = number
            break
        }
        number += 1
    }
    return answer
}
