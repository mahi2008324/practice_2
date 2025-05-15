#multiplication of n numbers
a=int(input("Enter the number : "))
mul_n=1
for i in range(1,a+1):
	   mul_n=mul_n * i
print("multiplication of numbers upto {} is : {}".format(a,mul_n))