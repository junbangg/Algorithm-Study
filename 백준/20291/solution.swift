let N = Int(readLine()!)!
var counter = [String: Int]()
for _ in 0..<N {
    let ext = readLine()!.split(separator: ".").compactMap{String($0)}[1]
    counter[ext, default: 0] += 1
}
let sortedCounter = counter.sorted { $0.0 < $1.0 }
for (key, val) in sortedCounter {
    print("\(key) \(val)")
}