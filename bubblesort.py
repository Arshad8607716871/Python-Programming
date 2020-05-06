b=[10,9,8,7,6,5,4,3,2,1]
x=len(b)
for i in range(x-1):
    for i in range(x-1):
        if b[i]>b[i+1]:
            temp=b[i+1]
            b[i+1]=b[i]
            b[i]=temp
print(b)