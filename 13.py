inpt = input()
inptSet = inpt.split(" ")
a = int(inptSet[0])
b = int(inptSet[1])
symb = str(inptSet[2])
for y in range(b):
    for x in range(a):
        if y == 0 or y == b - 1:
            print(symb, end="")
        else:
            if x == 0 or x == a - 1:
                print(symb, end="")
            else:
                print(" ", end="")
    print("")
