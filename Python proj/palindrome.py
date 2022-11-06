n=int(input("Enter unmber:"))
rev=0
t=n
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
if(rev==t):
    print("The num is a palindrome!")
else:
    print("The number isn't a palindrome!")