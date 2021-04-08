func binarySearchForAscending<T: Comparable>(array: [T], target : T) -> Int {
    var low = 0
    var high = array.count - 1
    
    while low <= high {
        let mid = (low + high) / 2
        let value = array[mid]
        if value == target {
            return mid
        } else if value > target {
            high = mid - 1
        } else {
            low = mid + 1
        }
    }
    
    return -1
}

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

var myArray = [1,2,3,4,5,6,7,9,10]
if let searchIndex = binarySearch(myArray, 5) {
    print("Element found on index: \(searchIndex)")
}
