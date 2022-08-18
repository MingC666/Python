import random
########################## TESTING VARIABLE ASSIGNMENT
fruits = ["apple", "banana","cherry"]
fruit1, fruit2, fruit3 = fruits
print(fruit1)
print(fruit2)
print(fruit3)

x, y, z = 10, 20, 30
print(x)
print(y)
print(z)

x=y=z = 10, 20, 30
print(x)
print(y)
print(z)

######################### RANDOM NUMBER
print("Now creating 10 random numbers from 1 ~19:")
i=0
while i<10:
	print(random.randrange(1,20)) #[1, 20)
	i += 1

######################### STRING QUOTE
""" This is  multiple
	lines comment"""
print("\n\nString testing:")
s =  """the paragraph will be
		split into 
	some special
format"""
print("the length is:", len(s))
print(s)
if "some" in s:
	print("the word 'some' is in text")
if "handsome" not in s:
	print("the word 'handome' not in text")

######################## string index testing
s = "0123456789"     #-1 for '9' 
print(s[:5])
print(s[2:5])
print(s[2:])

s = "9876543210"
print(s[-5:-2])
