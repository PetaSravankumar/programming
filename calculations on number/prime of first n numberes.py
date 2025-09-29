def prime(n):
    sum=0
    for i in range(1,n+1,1):
        if n%i==0:
            sum=sum+1
    if n==2:
        return n
    else:
        return 0   
n=int(input("n"))
count=0
while count<n:
    num=prime(count)
    if num>0:
        count+=1