x=int(input("Enter the age of 1 person"))
y=int(input("Enter the age of 2 person"))
z=int(input("enter the age of 3 person "))
if x>y and x>z:
    print("x is the oldest one")
elif y>z and y>x:
    print("y is the oldest one")
elif z>x and z>y:
    print("z is the oldest one")
if x<y and x<z:
    print("x is the youngest one")
elif y<x and y<z:
    print("y is the youngest")
elif z<x and z<y:
    print("z is the youngest")
else :
    print("all are of same age")

    