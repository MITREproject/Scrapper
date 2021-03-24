# Arrange the odd and even separately Even one’s first,odd ones later
# 1,3,2,5,6,4,7,8,9
# Output will be odd 1st and then even.

a = []
#accepting user input
size = int(input("How many elements do you want to enter? "))
for i in range(1, size+1):
	a.append(int(input("Enter element " + str(i) + " ")))


even = [] #list for storing even numbers
odd = [] #list for storing odd numbers

#categorizing the numbers as odd and even
for no in a:
	if no % 2 == 0:
		even.append(no)
	else:
		odd.append(no)

#sorting the lists
even.sort()
odd.sort()

odd.extend(even) #appending even part to the odd part
print(odd) #printing the result

