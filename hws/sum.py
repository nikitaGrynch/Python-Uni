while True:
    x = None
    y = None
    while x is None:
        try:
            x = int(input("Enter x = "))
        except ValueError:
            print("That's not a number!")
            x = None
        else:
            if x < 0:
                print("The number must be positive!")
                x = None
    while y is None:
        try:
            y = int(input("Enter y = "))
        except ValueError:
            print("That's not a number!")
            y = None
        else:
            if y < 0:
                print("The number must be positive!")
                y = None
            elif y == x:
                print("The number must be different from the first one!")
                y = None
    print("%.1f + %.1f = %.1f" % (x, y, x + y))
    print("--------------------")
    print()