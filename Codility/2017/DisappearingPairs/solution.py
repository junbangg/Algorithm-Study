## TC
# 'AC' -> 'AC'
# 'ACCA' -> ''
# 'ABC' -> 'ABC"
# 'ABBA' -> ''
# 'ABCCC' -> 'ABC"
# 'ABCCB' -> 'A'
# '' -> ''
# 'ABCC' -> 'AB

def solution(S):
    def recurse(string):
        if not string or len(string) == 1:
            return string
        for i in range(1, len(string)):
            if string[i-1:i+1] in ['AA', 'BB', 'CC']:
                if i == len(string) - 1:
                    string = string[:i-1]
                else:
                    string = string[:i-1] + string[i+1:]
                return recurse(string)
        return string
    return recurse(S)

