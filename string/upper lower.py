s=input("string :")
a=""
for i in s:
    if i>="A" and i<="Z":
        a=a+(chr(ord(i)+32))
    elif i==" ":
        a=a+i
    else:
        a=a+(chr(ord(i)-32))
print(a)