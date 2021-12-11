// Integer -> Binary String
let N = String(N, radix: 2)
// Binary String ->  Integer
let N = Int(strtoul("1111000", nil, 2))

// Array indexing
//Insert
A.insert("somthing", at: 0)

//Pop()
A.removeLast()

// Access Last element
A.last

// Count element Frequencies in Array
// Python Counter
let items = ["a","b","c","c"]
let mappedItems = items.map{ ($0, 1) }
let counts = Dictionary(mappedItems, uniquingKeyswith: +)

// Count unique values in Array
return Set(array).count
