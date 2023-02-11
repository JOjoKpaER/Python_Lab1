import sys

n, mx, mn = 0, -sys.maxsize - 1, sys.maxsize
upperBoundHeight = 190
lowerBoundHeight = 150
while True:
    inpt = input()
    if inpt == '!':
        break
    else:
        inpt = int(inpt)
        if upperBoundHeight >= inpt >= lowerBoundHeight:
            n += 1
            if inpt > mx:
                mx = inpt
            if inpt < mn:
                mn = inpt
print("\n", n, "\n", mn, " ", mx)
