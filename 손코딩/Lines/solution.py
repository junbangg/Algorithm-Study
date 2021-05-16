

#abc defg hijkl mnop, 5

def linesAndSpaces(s, limit):
    answer = ''
    count = 1
    for c in s:
        if c == ' ' or count == limit:
            answer += '\n'
            count = 1 
        else:
            answer += c
            count += 1

    return answer

# Recursion
def line_edit(s, maxLine):
    if not s or not maxLine or len(s) < maxLine:
        return s
    for i in range(maxLine - 1, 0, -1):
        if s[i] == ' ':
            return s[:index] + '\n' + line_edit(s[index:].lstrip(), maxLine)
    return s[:index] + '\n' + line_edit(s[index:].lstrip(), maxline)

a = 'abc def ghdddddd fffff'
limit = 5
print(linesAndSpaces(a, limit))
