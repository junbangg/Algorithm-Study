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


