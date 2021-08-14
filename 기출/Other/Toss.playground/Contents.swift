import Foundation

//import Foundation
//
//func solution(_ stepCounts:[Int]) -> Int {
//    var total: Int = 0
//    var bonus: Int = 0
//    var counter: Int = 0
//    for step in stepCounts {
//        var temp = step
//        if step > 10000 {
//            temp = 10000
//        }
//        total += temp
//        bonus += temp
//        if bonus >= 10000 {
//            counter += 1
//            print("got 10000")
//            if counter == 1 || counter == 3 || counter == 5 {
//                total += 10000
//                //bonus = 0
//            }
//            bonus %= 10000
//        }
//        print("total: \(total)")
//        print("bonus: \(bonus)")
//    }
//    return total
//}


//import Foundation
//
//extension String {
//    func subString(from: Int, to: Int) -> String {
//       let startIndex = self.index(self.startIndex, offsetBy: from)
//       let endIndex = self.index(self.startIndex, offsetBy: to)
//       return String(self[startIndex..<endIndex])
//    }
//}
//
//func solution(_ n:Int, _ keyInputs:[Int]) -> String {
//
//    var length: Int = 0
//    var answer: String = ""
//    for num in keyInputs {
//        if num == -1 {
//            answer = String(answer.dropLast())
//            if length > 0 {
//                length -= 1
//            }
//        } else if num == -2 {
//            answer = ""
//            length = 0
//        } else {
//            answer += String(num)
//            length += 1
//        }
//    }
//    if length < 4 {
//        return ""
//    }
//    else {
//        return answer.subString(from:0,to:n)
//    }
//}

