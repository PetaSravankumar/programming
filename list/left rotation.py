# l=[10,20,30,40,50]
# print(l)
# rotation=int(input("enter the number of rotations"))
# n=len(l)
# count=0
# while count<rotation:
#     temp=l[0]
#     for i in range(0,n-1,1):
#         l[i]=l[i+1]
#     l[n-1]=temp
#     count+=1
# print(l)

l=[10,20,30,40,50]
r=12
n=len(l)
r=r%n
for j in range(r,n-1+1,1):
    print(l[j],"",end="")
for i in range(0,r-1+1,1):
    print(l[i]," ",end="")
