''' to print multipliacation table of a given number by using fuction'''
def multi(a):
    product=1
    for i in range(11):
        product=a*i
        print (f"{a}*{i}={product}")
a=int(input("enter the nnumber"))
multi(a)
