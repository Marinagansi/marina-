
'''13. Given three integers, print the smallest one. (Three integers should be user input)'''
a=int(input("enter the integer:"))
b=int(input("enter the integer:"))
c=int(input("enter the integer:"))
if a>b<c:
    print(f'b is smallest')
elif b>a<c:
    print(f'a is smallest')
elif b>c<a:
    print (f'c is a smallest')