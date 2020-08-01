# Creating A Basic Function

### Code
```python
def x ():
	print("hello world")
x()
```

Here `def` keyword is used to define function.

We can use any name for `function` as we use in `variables`.

`x()` is used to call function `x`.

Function should be call after declaration.

***

# Passing Arguments To A Function

## Passing Basic Arguments
### Code
```python
def sum(a, b):
	print(a + b)
sum(2,5)
```

Here `a` and `b` are two arguments.

When we call function by `sum(2,5)` `2` and `5` got assign to `a` and `b` respectively.

***

## Giving Default Value To Arguments
### Code
```python
def greetings(name, greet = "Hii"): #greet has default value of "Hii"
	print(greet, name)
greetings("CodE-DowN", "Hello")
greetings("PythoN") #No second argument so greet has his default value "Hii"
```

Here Argument `greet` has default value `Hii`...

When no argument is passed inplace of `greet` for ex :- `greetings("PythoN")` then `greet` has his default value `Hii`.