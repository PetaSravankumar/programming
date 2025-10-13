n=input("str:")
a=len(n)
b=list(n)

for i in range(0,a//2,1):
    b[i],b[a-i-1]=b[a-i-1],b[i]
n=""
for j in b:
    n+=j
print(n)