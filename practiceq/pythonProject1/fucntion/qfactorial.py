'''find factorial num'''
def fact(a):
   product=1
   for i in range(2,a+1):
      product=product*i
   return product
a=int(input("enter the number:"))
c=fact(a)
print(f"the ans is{c}")