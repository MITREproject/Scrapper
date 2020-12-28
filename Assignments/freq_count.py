# Write program for below
# Count of Words
# {hello, hi, hello , Good , Bad, Good}
# O/p will be 
# hello -2 
# hi - 2
# Good - 2
# Bad - 1

import collections

words = ["hello", "hi", "hello", "good", "bad", "good"]
unique = []

#using built in library
counter = collections.Counter(words)
print("Method 1")
print(counter)
print()
print("Method 2")

#manual method
for word in words:
	if word not in unique:
		unique.append(word)

for word in unique:
	print(word, " : ", words.count(word))

#print(unique)
