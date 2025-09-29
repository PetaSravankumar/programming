n=int(input("eneter the number:"))
for i in range(1,n+1):
    print(i*2,end=" ")
print()

for i in range(2,n*2+1,2):
    print(i,end=" ")
# count=0
# num=0
# while num<n:
#     if count%2==0:
#         print(count,end="")
#         num+=1
#     count+=1