#multiplication table
a=int(input("Enter the number : "))
multi=1
for i in range(1,11):
	   multi=a * i
	   print("{} * {} = {}".format(a,i,multi)) 