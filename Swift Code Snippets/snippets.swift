//MARK: Integer -> Binary String
let N = String(N, radix: 2)
// Binary String ->  Integer
let N = Int(strtoul("1111000", nil, 2))

//MARK: Array indexing
//Insert
A.insert("somthing", at: 0)

//MARK: Pop()
A.removeLast()

//MARK: Access Last element
A.last

//MARK: Count element Frequencies in Array
// Python Counter
let items = ["a","b","c","c"]
let mappedItems = items.map{ ($0, 1) }
let counts = Dictionary(mappedItems, uniquingKeyswith: +)

//MARK: Count unique values in Array
return Set(array).count

//MARK: Substring Extension
//Reference: https://stackoverflow.com/a/46634511
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

//MARK: String -> Array
let str = "aBcDeF"

// Character형을 요소로 갖는 배열
let charArr = str.map {$0}
print("\(charArr) : \(type(of: charArr))") // ["a", "B", "c", "D", "e", "F"] : Array<Character>


// String형을 요소로 갖는 배열
let strArr = str.map {String($0)}
print("\(strArr) : \(type(of: strArr))") // ["a", "B", "c", "D", "e", "F"] : Array<String>

//MARK: Array -> String
let array = ["A", "B", "C"]
let str1 = String(Array)
let str2 = array.joined(separator: "")
let str3 = array.reduce("", +)

//MARK: 접두어 접미어 확인
let str = "aBcDeF"

// 접두어 (앞에서부터 몇 글자)
print(str.prefix(3)) // aBc
print(str.prefix(4)) // aBcD

// 접미어 (뒤에서부터 몇 글자)
print(str.suffix(1)) // F
print(str.suffix(2)) // eF


let str = "aBcDeF"

// 접두어 (앞에서부터 몇 글자)
print(str.hasPrefix("a"))  // true
print(str.hasPrefix("aB")) // true
print(str.hasPrefix("ab")) // false

// 접미어 (뒤에서부터 몇 글자)
print(str.hasSuffix("F"))  // true
print(str.hasSuffix("DeF")) // true
print(str.hasSuffix("FeD")) // false
