def func1(fname, lname):
	print("My name is {} {} ".format(fname, lname))
	print("Her name is " + fname + " " + lname)
func1("hanhan", "xiong")


def func2(*car):
	print("There are " + ": " + car[0] + ", " + car[1])
func2("Lexus", "BMW")

def func3(length, width):
	print("width is " + str(width) + "," + "length is " + str(length))
func3(width=10, length=20)

def func4(**car):
	print("It is " + car['year'] + " " + car['color'] + " " + car['brand'])
func4(color='white', brand='BMW', year='2020')

def func5(name="none"):
	print("user name is " + name)
func5("wasabi")
func5()

def func6(food):
	print("there are " + str(len(food)) + " food: ")
	for x in food: print(x)
func6(["apple", "banana", "watermelon"])

def func7():
	pass
func7()


def fib(n):
	if n==0:
		return 0
	if n==1:
		return 1
	else:
		return fib(n-1) +fib(n-2)
#print("fibbnacci of 5 is: " + str(fib(5))
a=fib(5)
print(a)
