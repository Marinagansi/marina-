'''wap which accepts marks of four subject and display total maraks, percentage and grade.'''
eng=int(input("mark of eng:"))
nep=int(input("mark of nep:"))
sci=int(input("mark of sci:"))
math=int(input("mark of math:"))

total_mark=eng+nep+sci+math
print(f'the total mark is',total_mark)
percentage=total_mark/400*100
print(percentage,"% ")
if percentage>70:
    print("distiction")
elif percentage>60:
    print("first division")
elif percentage>40:
    print("pass")
elif percentage<40:
    print("fail")
grade= percentage/100*4
print(grade,"grade")
