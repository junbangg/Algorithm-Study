output = []
n = input("ENter number: ")
m = input("Enter how many")
for _ in range(m):
    output.append(n)


f = open("testCase.txt")
f.write(output)
f.close()

