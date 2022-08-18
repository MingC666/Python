list1 = ['pen', 'eraser', 'laptop', 'airpot']
list2 = ['apple', 'orange', 'peach', 'watermelon']
list2.pop(2)
list2.remove('apple')
list2.insert(0,'grap')
del list1[2]

# copy list1 to list3
list3 = [x for x in list1]
#list3 = list(list1)
#list3 = list1.copy()

# add list2 to list 3
list3.extend(list2)
#for x in list2
# list3.append(x)
#list3 = list1+list2
list3.pop(2)

print(list1)
print(list2)
print(list3)

# sort
list3.sort()
print(list3)

#reverse sort
list3.sort(reverse=True)
print(list3)
