# creating an empty list
lst = []
# number of elemetns as input
n = int(input("Enter number of elements : "))
#t = int(input("Enter return type(1 for int 2 for string : "))
# iterating till the range
for i in range(0, n):
    ele = input()
    #if t == 1:
        #ele = int(ele)
    lst.append(ele) # adding the element

f = open("testCase.txt", "a")
f.write("[")
for num in lst:
    f.write(str(num))
    f.write(",")
f.write("]")
f.close()

