s1 = {"bird", "cat", "dog"}
s1.add("egle")
s1.update({"panda", "lion"})

s2 = {"bear", "dot", "zabra", "griff", "cat"}

s3 = s1.intersection(s2)
s4 = s1.copy()
s4.pop()
s4.intersection_update(s2)
s5 = s1.copy()
s5.remove("cat")
s5.symmetric_difference_update(s2)

print("s1:")
for x in s1:
	print(x)

print("s2:")
for x in s2:
	print(x)

print("s1 intersection s2")
for x in s3:
	print(x)

print("similar  above")
for x in s4:
	print(x)
print("s1 symmetric difference match s2:")
for x in s5:
	print(x)
