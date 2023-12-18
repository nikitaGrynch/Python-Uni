x = 10
x, y = 10, 20

x, y = y, x         # swap
x, y = y, x + y     # Fibonacci

s = "Hello, %s!" % "world" 
s = "x = %d, y = %d" % (x, y)
s = f"x = {x}, y = {y}" # Imperative style

######################

x, y  = 14, 6
print("%d + %d = %f" % (x, y, x + y))
print("%d - %d = %f" % (x, y, x - y))
print("%d * %d = %f" % (x, y, x * y))
print("%d / %d = %f" % (x, y, x / y))
print("%d %% %d = %f" % (x, y, x % y))
print("%d ** %d = %f" % (x, y, x ** y))
print("%d // %d = %f" % (x, y, x // y))

######################
if x > 2 and y > 2:
    print("Both > 2")
elif x > 2 or y > 2:
    print("One of them > 2")
elif not x > 2:
    print("x not > 2")
else:
    print("nothing > 2")

######################
while y < 0 :
    print(y, end=" ")
    y -= 1
else:
    print()

for i in range(10, 1, -1) :
    print(i, end=" ")
print()