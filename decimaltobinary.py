x=int(input("Enter Decimal No."))
list=[]
while(x!=1):
    y=x%2
    list.append(y)
    x=x//2
list.append(1)
print("Your Binary No. is",list[::-1])