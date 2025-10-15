s=input("string :")
a=""
for i in s:
    if i>="A" and i<="Z":
        a=a+(chr(ord(i)+32))
    else:
        a=a+(chr(ord(i)-32))
print(a)