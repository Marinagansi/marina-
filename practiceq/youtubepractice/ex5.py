#given a list iterate it an ddisplay number divisible by 5 if you
# find a number greater than 150  stop the loop iteration
list=[12,15,32,42,55,75,122,132,150,180,200]
for i in list:
    if i>150:
        break
    if i%5==0:

        print(i)