n=int(input("eter the number :"))
product=1
while n!=0:
    r=n%10
    n=n//10
    product=product*r
print(product)