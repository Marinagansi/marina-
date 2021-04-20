#given a number count the total number of the digit in a number
num=int(input("enter the num:"))
count=0
while num!=0:
    num//=10
    count+=1
print("the total no is",count)


num=int(input("num"))
while num>0:
    rem=num%10
    print(rem)
    num=num//10
    
