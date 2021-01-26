func solution(_ s:String) -> String {
    return String(s.sorted(){$0 > $1})
}
