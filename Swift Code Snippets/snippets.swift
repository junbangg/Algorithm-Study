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

/// Substrings!!!!
// Swift4/5
public extension String {
  subscript(value: Int) -> Character {
    self[index(at: value)]
  }
}

public extension String {
  subscript(value: NSRange) -> Substring {
    self[value.lowerBound..<value.upperBound]
  }
}

public extension String {
  subscript(value: CountableClosedRange<Int>) -> Substring {
    self[index(at: value.lowerBound)...index(at: value.upperBound)]
  }

  subscript(value: CountableRange<Int>) -> Substring {
    self[index(at: value.lowerBound)..<index(at: value.upperBound)]
  }

  subscript(value: PartialRangeUpTo<Int>) -> Substring {
    self[..<index(at: value.upperBound)]
  }

  subscript(value: PartialRangeThrough<Int>) -> Substring {
    self[...index(at: value.upperBound)]
  }

  subscript(value: PartialRangeFrom<Int>) -> Substring {
    self[index(at: value.lowerBound)...]
  }
}

private extension String {
  func index(at offset: Int) -> String.Index {
    index(startIndex, offsetBy: offset)
  }
}

// Usage
let text = "Hello world"
text[0] // H
text[...3] // "Hell"
text[6..<text.count] // world
text[NSRange(location: 6, length: 3)] // wor
