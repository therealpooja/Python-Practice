#fibonacci
print("Welcome to hte fibonacci series")
n1=int(input("Enter the ifrst numer"))
n2=int(input("Enter the second number"))
noft=int(input("Enter the rangeor number of terms "))
print(n1,n2)
while(noft-2):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)
    noft=noft-1