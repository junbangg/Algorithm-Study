// Solution in swift
func solution(_ num:Int) -> Int {
    var num = num
    var count = 0
    while num > 1 {
        if count == 500 {
            count = -1
            break
        }
        if num % 2 == 0 {
            num /= 2
        }
        else {
            num = 3 * num + 1
        }
        count += 1
    }
    return count 
}
