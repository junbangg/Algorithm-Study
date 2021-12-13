func findIndices(of digit: String, in string: String) -> [Int] {
    var indexArray: [Int] = []
    for (index, digit) in string.enumerated() {
        if digit == "5" {
            indexArray.append(index)
        }
    }
    return indexArray
}

func getSubstring(of string: String, without deleteIndex: Int) -> String {
    var substring = string
    let index = substring.index(substring.startIndex, offsetBy: deleteIndex)
    substring.remove(at: index)
    return substring
}

public func solution(_ N : Int) -> Int {
    let numberString = String(N)
    let indexArray = findIndices(of: "5", in: numberString)
    var answer = -Int.max

    for index in indexArray {
        let substring = getSubstring(of: numberString, without: index)
        guard let convertedNumber = Int(substring) else {
            break
        }
        answer = max(answer, convertedNumber)
    }
    return answer
}
//
//let test = 100
//solution(test)

//let number = 1598
let number = 15958
solution(number)

