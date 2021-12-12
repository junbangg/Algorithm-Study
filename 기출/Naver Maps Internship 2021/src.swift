import Foundation
/// 1
//func calculateDigitSum(of n: Int) -> Int {
//    var sum = 0
//    var number = n
//    while number != 0 {
//        sum = sum + number % 10
//        number = number / 10
//    }
//    return sum
//}
//
//public func solution(_ N : Int) -> Int {
//
//    var number = 1
//    var answer = 0
//    while true {
//        if calculateDigitSum(of: number) == N {
//            answer = number
//            break
//        }
//        number += 1
//    }
//    return answer
//}

/// 2
//func findIndices(of digit: String, in string: String) -> [Int] {
//    var indexArray: [Int] = []
//    for (index, digit) in string.enumerated() {
//        if digit == "5" {
//            indexArray.append(index)
//        }
//    }
//    return indexArray
//}
//
//func getSubstring(of string: String, without deleteIndex: Int) -> String {
//    var substring = string
//    let index = substring.index(substring.startIndex, offsetBy: deleteIndex)
//    substring.remove(at: index)
//    return substring
//}
//
//public func solution(_ N : Int) -> Int {
//    let numberString = String(N)
//    let indexArray = findIndices(of: "5", in: numberString)
//    var answer = -Int.max
//
//    for index in indexArray {
//        let substring = getSubstring(of: numberString, without: index)
//        guard let convertedNumber = Int(substring) else {
//            break
//        }
//        answer = max(answer, convertedNumber)
//    }
//    return answer
//}
////
////let test = 100
////solution(test)
//
////let number = 1598
//let number = 15958
//solution(number)

///3
public func solution(_ M : Int, _ N : Int) -> Int {
    let x = Int(sqrt(Double((4 * N) + M)))
    var answer = 0
    if x % 2 == 0 {
        answer = x
    } else {
        let maximumNSquares = (x-1) * (x-1) / 4
        let usableNSquares = min(maximumNSquares, N)
        if 4 * usableNSquares + M < x * x {
            answer = x - 1
        } else {
            answer = x
        }
    }
    return answer
}

solution(13, 3)

