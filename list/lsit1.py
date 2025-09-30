from itertools import zip_longest
a=[1,[2,3],[[3,2],[4,3]],5]
b=[]
for i in range(0,len(a),1):
    if i!='[':
        b.append(a)
print(a)