x=int(input("Enter how many prime no. you want to print"))
m=0
i=2
while i>0:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
        m=m+1
        if m==x:
            break

    i=i+1