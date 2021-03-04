#N students take  K apples and distribute them among each other evenly .
# the remaining (the undivisible) part remains  ih the basket .
# how many apples will each single student get?
#how many apples will remain  in the basket?
#the program reads the number N and K .
#it should print the two number for the question above.

N=int(input("enter the number of student in class"))
k=int(input ("enter the number of apples"))
apples_get=(k/N)
remaining_apples=(k%N)
print(f"each student got{apples_get}")
print(f"the remaining apples are {remaining_apples}")
