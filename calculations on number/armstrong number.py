n=int(input("n:"))
save=n
len=0
while n!=0:
    r=n%10
    n=n//10
    len=len+1
n=save
sum=0
while n!=0:
    r=n%10
    n=n//10
    sum=sum+(r**len)
print(sum)
if sum==save:
    print("armstrong")
else:
    print("not a armstrong")