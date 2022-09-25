x=int(input("enter how many odd natural number you want to print"))
x=x+x+2
i=1
while i<x:
    if(x%2!=0):
        print(x)
        x-=1
    else:
        x-=1
    
