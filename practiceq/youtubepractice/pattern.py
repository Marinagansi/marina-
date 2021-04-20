#1
#12
#123
#1234
#12345
for i in range(5):
    for j in range(i+1):
        print(j+1, end=" ")
    print()
#1
#21
#321
#4321
#5321
for i in range(5):
     for j in range(i,-1,-1):
         print(j+1, end=" ")

     print()

for i in range(1,6):
    for j in range(i,-1,-1):
       print(i+1, end=" ")
    print()