import Foundation

let NK = readLine()!.split(separator: " ").compactMap { Int($0) }
let N = NK[0]
let K = NK[1]
let number = Int(readLine()!)
let digits = String(number).compactMap { Int(String($0)) }

print(digits)