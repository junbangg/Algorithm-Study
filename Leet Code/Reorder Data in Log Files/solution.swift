class Solution {
    func reorderLogFiles(_ logs: [String]) -> [String] {
        var digitLogs: [String] = []
        var letterLogs: [String] = []

        for log in logs {
            let data = log.split(separator: " ")
            if data[1].isdigit() {
                digitLogs.append(data)
            } else {
                letterLogs.append(data)
            }
        }
        print(digitLogs)
        print(letterLogs)
        return ["asd"]
    }
}