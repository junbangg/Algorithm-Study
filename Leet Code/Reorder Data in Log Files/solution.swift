extension String {
    var isNumeric: Bool {
        return Double(self) != nil
    }
}

class Solution {
    func reorderLogFiles(_ logs: [String]) -> [String] {
        let numberLogs = logs.filter { $0.split(separator: " ").map { String($0) }[1].isNumeric }
        var letterLogs = logs.filter { !$0.split(separator: " ").map { String($0) }[1].isNumeric }

        letterLogs.sort(by: { (lhs, rhs) -> Bool in
            let lhsArray = lhs.split(separator: " ")
            let rhsArray = rhs.split(separator: " ")
            let lhsContents = String(lhsArray[1...].joined(separator: " "))
            let rhsContents = String(rhsArray[1...].joined(separator: " "))

            if lhsContents == rhsContents {
                return lhsArray[0] < rhsArray[0]
            }
            return lhsContents < rhsContents
        })

        return letterLogs + numberLogs
    }
}