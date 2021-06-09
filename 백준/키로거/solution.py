n = int(input())
answers = []
for _ in range(n):
    s = input()
    cursor = -1
    pword = []
    for c in s:
        if c == '<':
            if cursor > -1:
                cursor -= 1
        elif c == '>':
            if cursor < len(pword)-1:
                cursor += 1
        elif c == '-':
            if pword:
                if cursor == len(pword)-1:
                    pword.pop()
                    cursor -= 1
                else:
                    pword.pop(cursor)
        else:
            if cursor == len(pword)-1:
                pword.append(c)
            else:
                pword.insert(cursor+1, c)
            cursor += 1
    print(''.join(pword))