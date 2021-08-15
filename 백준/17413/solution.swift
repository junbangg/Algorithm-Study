let s = readLine()!

var tagSwitch: Bool = false 
var tag: String = ""
var word: String = ""
var substring: String = ""
var answer = [String]()
for c in s {
    if tagSwitch == true {
        if c == ">" {
            tag += ">"
            answer.append(tag)
            tag = ""
            tagSwitch = false
        } else {
            tag += String(c)
        }
    } else {
        if c == "<" {
            if !substring.isEmpty {
                word += String(substring.reversed())
                substring = ""
            }
            //reverse temp
            if !word.isEmpty {
                if word.last! == " "{
                    word.removeLast()
                }
                answer.append(word)
                word = ""
            }
            tagSwitch = true
            tag += "<"
            continue
        } else {
            if c == " " {
                if !substring.isEmpty {
                    word += String(substring.reversed())
                    word += " "
                    substring = ""
                }
            }
            substring += String(c)
        }
    }
}
if !substring.isEmpty {
    word += String(substring.reversed())
}
if !word.isEmpty {
    answer.append(word)
}
print(answer)