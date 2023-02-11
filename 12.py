n = int(input())
line = 1
j = 0
for i in range(n):
    print(i+1, end=" ")
    j += 1
    if j == line:
        print("")
        line += 1
        j = 0
