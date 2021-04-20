#i=0
#while i<11:
#     print(i)
 #    i+=1

for i in range(1,6):
        for j in range(1,i+1):
                print(j, end=" ")

        print()

num=int(input("enter the number:"))
sum=0
for i in range (1,num+1):
        sum=sum+i

print(f'sum is {sum}')