num=int (input ("enter the factorial number"))
product=1
for i in range (num,1,-1):
    product=product*i
print (f"the factorial is {product}")