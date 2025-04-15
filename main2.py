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

program = "EasyShopping"
budget = 1000
total = 866.43
quantity = 100
discount = 15
total2 = 736.47
tax = 20
total3 = 756.47
shipping = 29.99
total4 = 786.46

print(f"""User1: Hi! Welcome to {program}, how can I help?
      User2: Hey, I'm looking to buy {quantity} keychains for my small buisness; my budget is {budget} dollars.
      User1: Yeah Totally! Your total before shipping and tax fees is {total} dollars.
      User2: Hmm... It's actually my birthday today, I was looking to get a discount.
      User1: Sure! Our company offers {discount} percent discount off birthday orders.
      User2: Cool :)
      User1: Your new total is {total2} dollars!
      User2: How much are texes?
      User1: {tax} dollars, making tour total {total3} dollars.
      User2: Shipping fees?
      User1: So, because our product comes from south Asia, shipping is {shipping} dollars.
      User2: Yeah thats fine.
      User1: All right then, your grand total is {total4} dollars!
      User2: Okay, thank you so much! Have a good day! :D""")

# if conditionals
# if statements are used to check if a condition is true or false
# if condition is true, do something
# if condition is false, do something else

# if conditional statements always start with ifand depend on a boolean value (true or false)
# example
classSatrted = True #boolean variable
if classSatrted:
    print("class has started")
else:
    print("class has not started")

# logical and comparison operators
# == equal total!= not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# and logical operators
# or logical operators
# not logical operators
# example
age = 18
if age >= 18:
    print("you are an adult")
elif age == 17:
    print("you are almost and adult")
else:
    print("you are a minor")

# problem set #2
# 1. create a program that checks if a number
# is even or odd
# 2. ask user for a number
number = int(input("what is your number?"))
# 3. check if number is even or odd
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")