import Foundation

extension Int {
    func power(of number: Int) -> Int {
        return Int(pow(Double(self), Double(number)))
    }
}

func solution(_ dartResult:String) -> Int {
    var answer: [Int] = []
    var numberString = ""
    var number = 0
    var isSkill = false
    
    for (index, value) in dartResult.enumerated() {
        if value.isNumber {
            if index != 0 && isSkill {
                answer.append(number)
                isSkill = false
            }
            numberString += String(value)
        } else {
            if !isSkill {
                number = Int(numberString)!
                numberString = ""
            }
            isSkill = true
            if value == "D" { number = number.power(of: 2) }
            if value == "T" { number = number.power(of: 3) }
            if value == "*" {
                if !answer.isEmpty {
                    answer[answer.count - 1] *= 2
                }
                number *= 2
            }
            if value == "#" { number -= 2 * number }
        }
    }
    answer.append(number)
    
    return answer.reduce(0, +)
}

