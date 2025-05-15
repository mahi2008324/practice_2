#sum of odd numbers
a = int(input("Enter the number : "))
sum_odd = 0
for i in range(a + 1):
    if i % 2 != 0:
        sum_odd = sum_odd + i
print("sum of odd numbers upto {} is : {}".format(a, sum_odd))
