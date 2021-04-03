import Foundation
// Binary Search
func binarySearch<T:Comparable>(_ inputArr:Array<T>, _ searchItem: T) -> Int? {
    var lowerIndex = 0
    var upperIndex = inputArr.count - 1

    while (true) {
        let currentIndex = (lowerIndex + upperIndex)/2
        if(inputArr[currentIndex] == searchItem) {
            return currentIndex
        } else if (lowerIndex > upperIndex) {
            return nil
        } else {
            if (inputArr[currentIndex] > searchItem) {
                upperIndex = currentIndex - 1
            } else {
                lowerIndex = currentIndex + 1
            }
        }
    }
}

func solution(_ gift_cards:[Int], _ wants:[Int]) -> Int {
    //Sort arrays for Binary Search
	var gift_cards = gift_cards.sorted()
    var wants = wants.sorted()
    var answer = 0
    for i in 0...gift_cards.count - 1 {
        let target = gift_cards[i]
        /* firstIndex() = time complexity = O(n)
                  => total complexity = O(n^2)
        if let searched = wants.firstIndex(of: target) {
            wants.remove(at: searched)
        }
        */
        //Binary Search -> O(log n)
        //    Total Complexity = O(nlogn)
        if let searched = binarySearch(wants, target) {
            wants.remove(at: searched)
        }
    }
    return wants.count
}
