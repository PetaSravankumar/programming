l=[1,3,2,5,3,7]
sum=9
n=len(l)
for i in range(0,n-2+1,1):
    for  j in range(i+1,n-1+1,1):
        if l[i]+l[j]==sum:
            print([i,j])