fileprivate extension Dictionary where Key == Int, Value == Int {
    func contains(_ number: Int) -> Bool {
        guard self[number] != nil,
            self[number] != 0 else {
            print("false")
            return false
        }
        print("true")
        return true
    }
}

class Solution {
    func totalFruit(_ fruits: [Int]) -> Int {
        var maxAmount = 0
        var left = 0
        // var right = 0
        var dictionary: [Int: Int] = [:]
        var dictionaryCount = 0
        var fruitCount = 0
        
        for right in 0..<fruits.count {
            print("right", right)
            print(dictionaryCount)
            print(dictionary)
            if dictionaryCount == 2 && !dictionary.contains(fruits[right]) {
                print("left:", left)
                while left < right {
                    dictionary[fruits[left]]! -= 1
                    fruitCount -= 1
                    left += 1
                    // if dictionary[fruits[left]] != nil {
                    //     dictionary[fruits[left]] += 1
                    // } else {
                    //     dictionary[fruits[left]] = 1
                    // }
                    if dictionary[fruits[left-1]]! == 0 {
                        dictionaryCount -= 1
                        break
                    }
                }
                print("after left moves")
                print(dictionary)
            }
            
            if dictionary[fruits[right]] != nil {
                if dictionary[fruits[right]]! == 0 {
                    dictionaryCount += 1   
                }
                dictionary[fruits[right]]! += 1
            } else {
                dictionary[fruits[right]] = 1
                dictionaryCount += 1
            }
            fruitCount += 1
            
            maxAmount = max(maxAmount, fruitCount)
        }
        
        print(dictionary)
        return maxAmount
    }
}
/**
1, 1, 2, 3, 1, 1

maxNumber = 0
i, j
dictionary
dictionaryCount = 0
fruitCount = 0

i == 0
--------
j == 0 
1: 1
dictionaryCount = 1
fruitCount = 1

j == 1
1: 2
dictionaryCount = 1
fruitCount = 2

j == 2
1: 2
2: 1
dictionaryCount = 2
fruitCount = 3

j == 3
if dictionaryCount == 2 && !dictionaryContains(fruits[j]) {
    max update()

    while i < j && dictionaryCount == 2  {
        dictionary[fruits[i]] -= 1
        fruitCount -= 1
        i += 1
    }
    dictionaryCount -= 1
    break   
}

*/

// TC
// [0] -> 1
// [1, 1, 2, 3, 1, 1] -> 4

