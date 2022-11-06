#create a fun that will display how amny items are there in the list have names more than 5 characters

def function(names):
    n=0
    for i in names:
        k=len(i)
        if k>5:
            n+=1
    return n

names=["Pooja","Anusha","Anurag","Dev","Roy"]
c=function(names)
print(c)