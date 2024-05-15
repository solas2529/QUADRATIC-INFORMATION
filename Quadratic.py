

import math
print("Enter quadratic letters in order")
a = float(input("enter A number "))
b = float(input("enter B number "))
c = float(input("enter C number "))

print("y = " + str(a) + "x^2 + " + str(b) + "x + " + str(c))
print("y' = " + str(2 * a) + "x + " + str(b))
print("y\" = " + str(2 * a))
if (a == 0.0):
    print("Not quadratic")
elif (a > 0):
    if (b*b - 4*a*c < 0):
        print("There are no zeroes")
    else:
        zero1 = ((-b+math.sqrt(b*b - 4*a*c))/(2*a))
        zero2 = ((-b-math.sqrt(b*b - 4*a*c))/(2*a))
        print("Zeroes are at " + str(zero1) + " and " + str(zero2))
    min = ((-b)/(2*a))
    point = (a*min*min) + (b * min) + c
    print("Minimum is at (" + str(min) + ", " + str(point) + ")")

elif (a > 0):
    if (b*b - 4*a*c < 0):
        print("There are no zeroes")
    else:
        zero1 = ((-b+math.sqrt(b*b - 4*a*c))/(2*a))
        zero2 = ((-b-math.sqrt(b*b - 4*a*c))/(2*a))
        print("Zeroes are at " + str(zero1) + " and " + str(zero2))
    max = ((-b)/(2*a))
    point = (a*max*max) + (b * max) + c
    print("Minimum is at ()" + str(max) + ", " + str(point) + ")")



