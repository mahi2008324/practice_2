#multiplication of even numbers
a=int(input("Enter the number : "))
mul_even=1
for i in range(1,a+1):
	if i % 2 == 0:
	   mul_even=mul_even * i
print("multiplication of even numbers upto {} is : {}".format(a,mul_even))