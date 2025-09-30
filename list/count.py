l=[int(input("value:")) for i in range(int(input("size:")))]
print(l)
target=int(input("target:"))
count=0
for i in range(len(l)):
    if target==l[i]:
        count+=1
print(count)