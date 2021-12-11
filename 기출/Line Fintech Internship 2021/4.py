from itertools import combinations

# _set = set([i for i in range(15)])
test = list(combinations([i for i in range(15)], 9))
print(len(test))
# print(test)