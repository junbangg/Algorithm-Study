
def solution(pixels):
    # zero = ["111", "101", "101", "101", "111"]
    # one = ["110", "010", "010", "010", "111"]
    # two = ["111", "001", "111", "100", "111"]
    # three = ["111", "001", "111", "001", "111"]
    # four = ["101", "101", "111", "001", "001"]
    # five = ["111", "100", "111", "001", "111"]
    # six = ["111", "100", "111", "101", "111"]
    # seven = ["111", "101", "001", "001", "001"]
    # eight = ["111", "101", "111", "101", "111"]
    # nine = ["111",  "101", "111", "001", "111"]
    stringToNumber = {
        "111101101101111": "0",
        "110010010010111": "1",
        "111001111100111": "2",
        "111001111001111": "3",
        "101101111001001": "4",
        "111100111001111": "5",
        "111100111101111": "6",
        "111101001001001": "7",
        "111101111101111": "8",
        "111101111001111": "9"
    }

    numberOfDigits = len(pixels[0]) // 3
    x_end =  len(pixels)
    finalString = ""
    for num in range(numberOfDigits):
        y_start = num * 3
        y_end = y_start + 3
        numString = ""
        for x in range(x_end):
            for y in range(y_start, y_end):
                numString += pixels[x][y]
        finalString += stringToNumber[numString]
    return int(finalString)









