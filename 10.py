import math

while True:
    op = input()
    if "x" in op:
        print(op.split("x")[0])
        break
    try:
        if "+" in op:
            print(res := int(op.split("+")[0]) + int(op.split("+")[1]))
        if "-" in op and "!" not in op:
            print(res := int(op.split("-")[0]) - int(op.split("-")[1]))
        if "*" in op:
            print(res := int(op.split("*")[0]) * int(op.split("*")[1]))
        if "/" in op:
            print(res := int(op.split("/")[0]) // int(op.split("/")[1]))
        if "%" in op:
            print(res := int(op.split("%")[0]) % int(op.split("%")[1]))
        if "!" in op and "-" not in op and "." not in op:
            print(res := math.factorial(int(op.split("!")[0])))
    except ValueError:
        continue
