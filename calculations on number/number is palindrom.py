n=int(input("enter the num:"))
a=n
rev=0
while n!=0:
    r=n%10
    n=n//10
    rev=rev*10+r
if a==rev:
    print("num is palindrom")
else:
    print("num is not palindrom")
