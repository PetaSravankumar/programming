l=[int(input("value:")) for i in range(int(input("size:")))]
print(l)
sum=0
for i in range(len(l)):
    sum+=l[i]
    print(sum)