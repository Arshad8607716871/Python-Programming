b=[23,34,44,56,63,74]
x=int(input("Enter No. to be searched"))
def search():
    l=0
    u=len(b)-1
    while l<=u:
        mid=(l+u)//2
        if b[mid]==x:
            print("No. is found at location",mid+1)
            return
        else:
            if b[mid]>x:
                u=mid-1
            else:
                l=mid+1
    return 3
c=search()
if c==3:
    print("No. is not found")
