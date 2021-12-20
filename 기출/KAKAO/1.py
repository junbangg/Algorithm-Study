def solution(s):
    answer = ''
    dic = {'zero' : '0',
           'one' : '1',
           'two' : '2',
           'three' : '3',
           'four' : '4',
           'five' : '5',
           'six' : '6',
           'seven' : '7',
           'eight' : '8',
           'nine' : '9'}
    word, num = '', ''
    for c in s:
        if c.isdigit():
            num += c
            if word and word in dic:
                #convert to num and add to answer
                answer += dic[word]
                word  = ''
        elif c.isalpha():
            if num:
                # add to answer
                answer += num
                num = ''
            #check if s is valid number and add to result if it is
            if word in dic:
                answer += dic[word]
                word = ''
            word += c
    if num:
        answer += num
    if word:
        answer += dic[word]
    return int(answer)

s = "one4seveneight"
print(solution(s))
