import Foundation

/*
 * Complete the 'minimumNumber' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. STRING password
 */

func calculateMissingCharacters(hasDigit: Bool, hasLowerCase: Bool, hasUpperCase: Bool, hasSpecialCharacter: Bool) -> Int {
    var missingCharacterNumbers = 0
    if !hasDigit {missingCharacterNumbers += 1}
    if !hasLowerCase {missingCharacterNumbers += 1}
    if !hasUpperCase {missingCharacterNumbers += 1}
    if !hasSpecialCharacter {missingCharacterNumbers += 1}

    return missingCharacterNumbers
}

func minimumNumber(n: Int, password: String) -> Int {
    // Return the minimum number of characters to make the password strong
    let missingPasswordLength = 6 <= n ? 0 : 6 - n
    var hasDigit = false
    var hasLowerCase = false
    var hasUpperCase = false
    var hasSpecialCharacter = false
    let special_characters = "!@#$%^&*()-+"

    for char in password {
        if char.isNumber {
            hasDigit = true
        } else if char.isLowercase {
            hasLowerCase = true
        } else if char.isUppercase {
            hasUpperCase = true
        } else if special_characters.contains(char) {
            hasSpecialCharacter = true
        }
    }
    let missingCharacterAmount = calculateMissingCharacters(hasDigit: hasDigit,
                                                            hasLowerCase: hasLowerCase,
                                                            hasUpperCase: hasUpperCase,
                                                            hasSpecialCharacter: hasSpecialCharacter)

    return max(missingPasswordLength, missingCharacterAmount)
}

let stdout = ProcessInfo.processInfo.environment["OUTPUT_PATH"]!
FileManager.default.createFile(atPath: stdout, contents: nil, attributes: nil)
let fileHandle = FileHandle(forWritingAtPath: stdout)!

guard let n = Int((readLine()?.trimmingCharacters(in: .whitespacesAndNewlines))!)
else { fatalError("Bad input") }

guard let password = readLine() else { fatalError("Bad input") }

let answer = minimumNumber(n: n, password: password)

fileHandle.write(String(answer).data(using: .utf8)!)
fileHandle.write("\n".data(using: .utf8)!)

