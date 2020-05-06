x=int(input("Enter Ist number"))
y=int(input("Enter 2nd number"))
if(x>y):
	smaller=y
else: 
	smaller=x
for i in range(1,smaller+1):
	if((x%i==0) and (y%i==0)):
		gcd=i
print("GCD of Given no.",gcd)
	
