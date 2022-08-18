dic = {"brand": "Lexux", "model":"nx350", "year":2020}
print(dict)

print("length of dict:")
print(len(dic))


print("\nkeys of dict:")
print(dic.keys())

print("\nvalues of dict:")
print(dic.values())

print("\nitems in dict:")
print(dic.items())

dic.update({"color": "white"})
print("\nupdate the dict:")
print(dic)

dic.pop("color")
#del dic['color']
print("remove using del OR pop:")
#dic.popitem()
print("popitem remove last item:")
print(dic)

print("\nfor x in dictionary print keys only")
for x in dic:
	print(x)

print("\nusing [] to get values")
for x in dic:
	print(dic[x])
print("\n OR use x,y pair in dictionary.items():")
for x, y in dic.items():
	print(x, y)
