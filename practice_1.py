#sum of even numbers
a=int(input("Enter the number : "))
sum_n=0
for i in range(a+1):
	if i % 2 == 0:
	   sum_n=sum_n+i
print("sum of even numbers upto {} is : {}".format(a,sum_n))