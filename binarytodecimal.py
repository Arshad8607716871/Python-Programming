from array import *
x=int(input("Enter Size of your binary no."))
arr1=array('i',[])
result=0
b=0
for i in range(x):
    y=int(input("Enter {} Bit".format(i+1)))
    arr1.append(y)
for i in range(x-1,-1,-1):
    c=arr1[i]*(2**b)
    result=c+result
    b=b+1
print("Your Decimal No. is",result)

