def sum(a, b):
	print(a + b)
sum(2,5)


def greetings(name, greet = "Hii"): #greet has default value of "Hii"
	print(greet, name)

greetings("CodE-DowN", "Hello")
greetings("PythoN") #No second argument so greet has his default value "Hii"

def infinite(*x): #You can pass many arguments
	print(x)
	print(type(x)) #Tuple

infinite("CodE", 12, "PythoN")

def many(**y): #You can pass many arguments
	print(y)
	print(type(y)) #Dictionary

many(a = "Hii", b = "CodE-DowN")

def names(a):
	print(a)

y = ["CodE-DowN", "PythoN", 12, True]
names(y)