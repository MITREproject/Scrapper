# Input Array : [2, 3, 5, 4] Output Array: [60, 40, 24, 30] 
#Output [i] = Multiplication of all elements except 'i'th element.

a = []
#accepting user input
size = int(input("How many elements do you want to enter? "))
for i in range(1, size+1):
	a.append(int(input("Enter element " + str(i) + " ")))

mult = []
product = 1 #variable which stores product of entire array

for i in a:
	product *= i #calculating the product

for i in a:
	mult.append(int(product / i)) #removing ith element from product

print(mult) #printing the result