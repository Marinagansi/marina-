#what7 will be the output of the following program? rewrite the code using while loop to display same output
#i=0
#while i<5 :
#    if i==3:
#        break
#    print(i)
#    i+=1

  #what will be the output of following program? rewrite the code using for loop display same output
#n=5
#i=0
#while i<=n:
 #   i+=1
 #   if i==3:
  #      continue
   #     print (i)

#for i in range (0,6):
#   i+=1
 #   if i==3:
  #      continue
  #  print(i)
#the python code generate 50 random even integers.Rewrite the code so it uses a while loop insted for loop
import random
my_list= []
i=0
while i<=50:

    num=random.randint(1,200)
    if num%2==0:
        my_list.append(num)
    i+=1