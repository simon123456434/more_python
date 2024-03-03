# a task of a thousend functions
#as i am not the best at functions.... i may as well do loas of them untill i get them correct


def my_function(fname): #an argument can be passed into the braces.
  print(fname + "Hello from a function")


my_function("simon") # the name in the braces is stored in fname argument
my_function("carl")# argument changes.

#Parameters or Arguments?
#The terms parameter and argument can be used for the same thing: information that are passed into a function.
#From a function's perspective:
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the value that is sent to the function when it is called.

#Number of Arguments
#By default, a function must be called with the correct number of arguments.
# Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments,
# not more, and not less.


#example1

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


def cake(coffee_cake, sponge_cake):
  print(coffee_cake + " " +  sponge_cake)

# you can assighn a argument to the paramater by the = symbol ( did that my accident ). lol
cake(coffee_cake = "mine" , sponge_cake  = "also mine")


#Example
#This function expects 2 arguments, but gets only 1:

#def my_function(fname, lname):
#  print(fname + " " + lname)

#my_function("Emil")

# it will cause a issue.


#Arbitrary Arguments, *args
#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

#This way the function will receive a tuple of arguments, and can access the items accordingly:

#Example
#If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")



#Keyword Arguments
#You can also send arguments with the key = value syntax.

#This way the order of the arguments does not matter.

#Example
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def name(name1,name2, name3):
  print("my name is " +  name1)


name(name1 = "emms", name2 = "karen", name3 = "simon")

#Arbitrary Keyword Arguments, **kwargs
#If you do not know how many keyword arguments that will be passed into your function,
#add two asterisk: ** before the parameter name in the function definition.

#This way the function will receive a dictionary of arguments, and can access the items accordingly:

#Example
#If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


#Default Parameter Value
#The following example shows how to use a default parameter value.

#If we call the function without argument, it uses the default value:

#Example
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function() #<----
my_function("Brazil")



#Return Values
#To let a function return a value, use the return statement:

#Example
def my_function(x):
  return 5 * x  # <----------

print(my_function(3))
print(my_function(5))
print(my_function(9))


#in Python, a function can return a value using the `return` statement. Here's a simple example:


def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8

#In this example, the `add` function takes two arguments
#`a` and `b`, adds them together, and returns the result using the
#`return` statement. Then, we call the `add` function with arguments `3` and `5`,
#and store the returned value in the variable `result`, which we then print out.

#The pass Statement
#function definitions cannot be empty, but if you for some reason
#have a function definition with no content, put in the pass statement to avoid getting an error.

#Example
def myfunction():
  pass


#Positional-Only Arguments
#You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

#To specify that a function can have only positional arguments, add , / after the arguments:

#Example
def my_function(x, /):
  print(x)

my_function(3)


#Keyword-Only Arguments
#To specify that a function can have only keyword arguments, add *, before the arguments:

#Example
def my_function(*, x):
  print(x)

#make sure to show what the function returns

def fun() -> int:
  return 10


fun()

#make sure to do the same for lists.
def func(numbers: list[int]) -> list[int]:
  numbers.reverse()

  return numbers

#functions should be simple break the thing down and not have confusing

#add doc strings that is precise.

 #  """"""  