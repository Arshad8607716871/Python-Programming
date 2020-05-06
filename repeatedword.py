a=open("file.txt","r")
b=a.read()
c=b.split()
print(b)
dict={}
i=0
while ( i!=len(c) ):
    count=1
    for j in range(i+1,len(c)):
        if c[j]==c[i]:
            count+=1
        else:
            pass
    if c[i] in dict.keys():
        pass
    else:
        dict.update({c[i]:count})
    i+=1
m=max(dict.values())
for key,value in dict.items():
    if value==m:
        print(key)

