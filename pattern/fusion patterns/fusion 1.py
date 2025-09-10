n=4
for i in range(1,4+1,1):
    for j in range(1,i+1,1):
        print("*",end="")
    print("")
n=3
for i in range(1,3+1,1):
    for j in range(1,n-i+1+1,1):
        print("*",end="")
    print("")