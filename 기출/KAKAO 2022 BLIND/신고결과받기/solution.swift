import Foundation

func split(from string: String) -> (String, String) {
    let splitData = string.split(separator: " ").map { String($0) }
    return (splitData[0], splitData[1])
}

func solution(_ id_list:[String], _ report:[String], _ k:Int) -> [Int] {
    var answer = Array(repeating: 0, count: id_list.count)
    var reported_reporters: [String: Set<String>] = [:]
    var id_index: [String: Int] = [:]
    
    for (index, id) in id_list.enumerated() {
        id_index[id] = index
    }
    
//    report.forEach { data in
    for data in report {
        let (reporter, reported) = split(from: data)
        
        if reported_reporters[reported] != nil {
            reported_reporters[reported]!.insert(reporter)
        } else {
            reported_reporters[reported] = [reporter]
        }
    }
    
//    reported_reporters.forEach { (_, reporters) in
    for (_, reporters) in reported_reporters {
        if reporters.count >= k {
//            reporters.forEach { id in
            for id in reporters {
                answer[id_index[id]!] += 1
            }
        }
    }
    
    return answer
}
