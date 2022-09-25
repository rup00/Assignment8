x=int(input("enter how many odd natural number you want to print"))
ch=x*x
count=1
i=1
while i<=ch:
    if count<=x:
        if(i%5==0):
            print(i)
            count+=1
            i+=1
        else:
            i+=1
    
