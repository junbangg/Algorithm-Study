from collections import Counter

a = [1,2,3,4,3]
count = Counter(a)

print(count.most_common(1)[0][1])
