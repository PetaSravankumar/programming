a=[int(input("value")) for i in range(int(input("size:")))]
n=len(a)
for j in range(0,n-1+1,1):
    for i in range(0,n-2+1,1):
        if a[i]>a[i+1]:
            c=a[i]
            a[i]=a[i+1]
            a[i+1]=c
        print(a)
    print("")

for i in range(0,n-2+1,1):
        if a[i]>a[i+1]:
            c=a[i]
            a[i]=a[i+1]
            a[i+1]=c
        print(a)