#A school decided to replace the desk in three classroom . each desk sits two student . given the number of students
#in each class, print the smallest possible number of desk that can be purchased.
#the program should read three integers; the number of student in each 3 classes  a,b, and c respectively
#in the first test there are three groups. the first group has 20 student and thus needs 10 desk. the second group
#has 21 students, so they can get by with no fewer than 11 desks. 11 deskds are also enough for third group of 22 student
#so, we need 32 desks in total

class1= int (input ("enter the number of student in first class1:"))
class2= int (input("enter the number of student in second class2:"))
class3= int (input ("enter the number of student in third class3:"))
desk_class1=(class1//2)
print(f"the required number of desk for first class is {desk_class1}")
desk_class2=(class2//2)
print(f"the required number of desks for second class is {desk_class2}")
desk_class3=(class3//2)
print(f"the required number of desks for third class is {desk_class3}")

remain_class1= (class1%2)
print (f"remaining desk for first class is{remain_class1}")
remain_class2=(class2%2)
print(f"remaining desk for second class is {remain_class2}")
remain_class3 = (class3% 2)

print (f"remaining desk for third class is {remain_class3}")
total_desk=desk_class1 + desk_class2 + desk_class3 + remain_class1 + remain_class2 + remain_class3
print (f"total number of desk that can be purchased is {total_desk}")
