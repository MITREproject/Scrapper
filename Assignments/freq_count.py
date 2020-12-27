# Write program for below
# Count of Words
# {hello, hi, hello , Good , Bad, Good}
# O/p will be 
# hello -2 
# hi - 2
# Good - 2
# Bad - 1

import collections

words = []
#accepting user input
size = int(input("How many elements do you want to enter? "))
for i in range(1, size+1):
	words.append(str(input("Enter element " + str(i) + " ")))
unique = []

#using built in library
counter = collections.Counter(words)
print("---------------------------------------")
print("Method 1")
print(counter)
print("---------------------------------------")
print("Method 2")

#manual method
for word in words:
	if word not in unique:
		unique.append(word) #finding all the unique words

for word in unique:
	print(word, " : ", words.count(word))

#print(unique)
