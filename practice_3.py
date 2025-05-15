#sum of n numbers
a=int(input("Enter the number : "))
sum_n=0
for i in range(a+1):
	sum_n=sum_n+i
print("sum of first {} numbers is : {}".format(a,sum_n))