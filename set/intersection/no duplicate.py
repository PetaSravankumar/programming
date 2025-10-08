a=[1,2,3,4,1,5]
b=[1,2,6,4,5,9]
c=[]
for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)