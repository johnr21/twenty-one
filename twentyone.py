x = input("Enter a number: ")

if float(x) == 21:
    print("test")
elif float(x) > 21:
    print("test 2")
elif float(x) < 21:
    print("test 3")
elif type(x) is str:
    print("test 4")
else:
    print("test 5")
