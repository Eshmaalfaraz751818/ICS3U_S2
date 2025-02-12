import math

x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)
print("Now deciding if", y, "is a factar of", x, "...")
if y!=0:
  print("Yes!", y, "is a factar of", x)
  rem = x % y
  if rem == 0:
    print("Yes! remainder is 0" )
  else:
    print("The remainder is not 0")
else:
    print("No!", y, "is not a foctar of", x)
