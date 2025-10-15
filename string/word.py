s=input("enter the str:")
l=[]
a=""
for i in s:
    a=a+i
    if i==" ":
        l.append(a)
        a=""
l.append(a)
print(l)
a=""
for i in l:
    a=a+i+" "
print(a)