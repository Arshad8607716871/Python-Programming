b=[10,9,8,7,6,5,4,3,2,1]
a=len(b)
for i in range(a-4):
    min=b[i]
    for j in range(i+1,a):
        if  min>b[j]:
            min=b[j]
            loc=j
    temp=b[loc]
    b[loc]=b[i]
    b[i]=temp
print(b)