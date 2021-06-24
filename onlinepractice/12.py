"""A school decided to replace the desks in three classrooms. Each desk sits two students.
Given the number of students in each class, print the smallest possible number of desks
that can be purchased.
The program should read three integers: the number of students in each of the three
classes, a, b and c respectively.
Hint. In the first test there are three groups. The first group has 20 students and thus needs 10
desks. The second group has 21 students, so they can get by with no fewer than 11 desks.
11 desks are also enough for the third group of 22 students. So, we need 32 desks in total"""
class_a=int(input("enter the number of student:"))
class_b=int(input("enter the number of student:"))
class_c=int(input("enter the number of student:"))
a=class_a//2
print(f"in class a",a," bench are required")
b=class_b//2
print(f'in cals b',b,"bench are required")
c=class_c//2
print(f'in class c',c,"bench are required")
total=a+b+c
print(f'tatal bench are', total)

