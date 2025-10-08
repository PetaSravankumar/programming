l=[10,20,30,40,50]
n=len(l)
# ro=int(input("n:"))
# count=0
# i=0
# print(l)
# while count<ro:
#     temp=l[n-1]
#     for i in range(n-1,0,-1):
#         l[i]=l[i-1]
#     l[0]=temp
#     count+=1
# print(l)

r=12
r1=r%n
for i in range(n-r1,n-1+1,1):
    print(l[i]," ",end="")
for j in range(0,n-r1-1+1,1):
    print(l[j]," ",end="")