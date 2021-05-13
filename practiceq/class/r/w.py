
#read  a content of one file and write it into another file
f=open("test2.txt","r")
content=f.read()
f=open("test3.txt",'w')
f.write(content)
f.close()