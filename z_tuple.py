t1 = ("banana", "orange","peach", "apple")
t1 += ("cheery",)
t1 += ("watermelon", "peach")

(val1, *val2, val3) = t1
(temp1, *temp2) = t1

print(t1)
print(val1)
print(val2)
print(val3)
print(temp1)
print(temp2)
print(t1.count("peach"))
print(t1.index('peach'))
