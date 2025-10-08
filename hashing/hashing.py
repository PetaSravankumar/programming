pos=[0 for i in range(10)]
neg=[0 for i in range(10)]
n=int(input("enter the vlaue"))
for i in range(n):
    x=int(input("enter the value"))
    if x>=0:
        pos[x]=pos[x]+1
    else:
        neg[x*-1]=neg[x*-1]+1
print(pos)
print(neg)