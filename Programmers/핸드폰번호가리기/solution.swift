func solution(_ phone_number:String) -> String {
    let lastFour = phone_number.suffix(4)
    if phone_number.count == 4 {
        return String(lastFour)
    }
    var asterix = ""
    for _ in 0...phone_number.count - 5 {
        asterix += "*"
    }
    return asterix + lastFour 
}

func solution(_ phone_number:String) -> String {
    return String("\(String(repeating: "*", count: phone_number.count - 4))\(phone_number.suffix(4))")
}
