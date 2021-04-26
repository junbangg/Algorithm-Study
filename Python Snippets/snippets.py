'''
get key with maximum value in dictionary
https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
'''
max(dict, key = dict.get)

'''
remove punctuation from string
note that it is forward slash \  not /
'''
string = re.sub(r'[^\w]', ' ', originalString)


'''
Custom Sorting with lambda
example) sorting ["let1 art can", "let2 own kit dig"] by [1:] elements first and then the first element
'''
sort(key = lambda x: (x.split()[1:], x.split()[0]))

'''
Sorting each string inside list
'''
for i in range(len(string)):
    temp = sorted(string[i])
    string[i] = ''.join(temp)

