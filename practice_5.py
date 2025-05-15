#multiplication of odd numbers
a=int(input("Enter the number : "))
mul_odd=1
for i in range(1,a+1):
	if i % 2 == 1:
	   mul_odd=mul_odd * i
print("multiplication of odd numbers upto {} is : {}".format(a,mul_odd))