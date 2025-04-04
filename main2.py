# what are variables?

# there are different types of variables
# strings are text
name = "John" #quotation marks
name2 = "Lucy"
# intigers are whole numbers
num1 = "10" #no quotation marks
num2 = 20
print(int(num1) + num2) # when you have
# a plus sign between two variables its called
# concatenation
# type casting when you convert a
# variable from one type to another
# print(name +"and"+ name2 +"have"+ num1 + str(num2) + "apples")
# f strings allow us to insert variables into strings
# using f before the string
print(f"{name} and {name2} have {num1} apples")

# floats are decimal numbers
dollars = 10.99
# it can be positive or negative
print(f"{name} has {dollars} dollars")
# booleans are true or false
is_student = True
# it can be true or false
print(f"{name} is a student: {is_student}")
# lists are collections of values
# dictionaries are collections of key-value pairs
# problem set #1
# 1. create 5 different types of variables
# 2. print them out
# 3. use f strings to format the strings
name = "David"
name2 = "Edwin"
food = "Ice cream"
dollars = 2.99
dollars2 = 1.50
print(f"{name} and {name2} go to get {food} , {name} 's {food} costs {dollars} dollars, {name2} 's costs {dollars2} dollars.")