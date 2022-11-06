def function(num):
    even=0
    odd=0
    for i in num:
        if i %2==0:
            even=+1
        else:
            odd+=1
    return even,odd
num=[32,21,64,100,13]
even,odd=function(num)
print(even)
print(odd)