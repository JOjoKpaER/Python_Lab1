n = int(input())
for i in range(n+1):
    for k in range(n, i, -1):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print("")
