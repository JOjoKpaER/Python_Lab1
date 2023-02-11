while True:
    passwd = input()
    if passwd != input():
        print("Различаются.")
    else:
        if len(passwd) < 8:
            print("Короткий!")
        else:
            if "123" in passwd:
                print("Простой")
            else:
                break
print("OK.")
