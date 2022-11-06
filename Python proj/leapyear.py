a=int(input("Enter the year to be checked:"))
if((a%4==0)and(a%400==0)):
    print("The year is a leap year")
else:
    print("The year is not a leap year")