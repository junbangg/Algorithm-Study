
// func solution(_ id_list: [String], _ report: [String]) -> [String] {
//     var reporter_data : [String:[Int, ]]

// }
// var a : [String: [Any]]] = [:]

extension String {

    func substring(from: Int, to: Int) -> String {

        guard from < count, to >= 0, to - from >= 0 else {
            return ""
        }
        let startIndex = index(self.startIndex, offsetBy: from)
        let endIndex = index(self.startIndex, offsetBy: to + 1)

        return String(self[startIndex..<endIndex])
    }
    
}
var testing = "abcdefg"
let t1 = testing.substring(from: 0, to: 4)
print(t1)

var dic : [String:[Any]] = [:]

dic["hey"] = [1]
dic["hey"]!.append("1")
dic["hey"]!.append(23)
print(dic)