a=[int(input("value")) for i in range(int(input("size:")))]
n=len(a)
print(a)
for j in range(0,n//2,1):
   a[j],a[n-j-1]=a[n-j-1],a[j]
print(a)