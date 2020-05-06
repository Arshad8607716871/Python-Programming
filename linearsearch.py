
b=[23,43,54,64,62,15]
x=int(input("Enter no. to be searched"))
def linearsearch():
    for i in range(6):
        if b[i]==x:
            print("No. is found at location",i+1)
            return
    return 3
c=linearsearch()
if c==3:
    print("No. is not found")