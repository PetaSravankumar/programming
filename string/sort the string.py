a=input("Enter the string")
b=list(a)
n=len(a)
for j in range(0,n-1+1,1):
    for i in range(0,n-2+1,1):
        if b[i]>b[i+1]:
            c=b[i]
            b[i]=b[i+1]
            b[i+1]=c
 a=""
for i in b:
    a+=i
print(a)
