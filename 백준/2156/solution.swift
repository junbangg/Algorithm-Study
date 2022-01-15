readLine()
var arr = [0,0,0]
arr[0] = Int(readLine()!)!

while let input = readLine() {
    let wine = Int(input)!
    let t = arr[2]

    arr[2] = max(arr[0], arr[1], arr[2])
    arr[1] = arr[0] + wine
    arr[0] = t + wine
}

print(arr.max()!)
