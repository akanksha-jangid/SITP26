# ##Assignment 4

# ##In python ,data types defines the type of value a variable can store
# #### Variables can store data of different types, and different types can do different things.


#1 INTEGER: An integer is a whole number without a decimal point.
# It can be positive, negative, or zero. 
# Syntax : variable_name = integer_value
##example:
a = 10
b = -25
c = 0

print(a)
print(type(a))

# ####Features
# # No decimal point
# # Supports arithmetic operations
# # Unlimited length in Python

# # 2. Float (float)

# # A float is a number with a decimal point.

# # Syntax :variable_name = float_value

# # Features
# # Stores decimal values
# # Used in scientific calculations
# # More precise than integers for fractional values

pi = 3.14
temperature = -12.5

print(pi)
print(type(pi))
####3String (str)
# A string is a sequence of characters enclosed in quotes.
# Syntax :variable_name = "text"

# # Features
# # Used to store text
# # Immutable (cannot be changed directly)
# # Supports indexing and slicing

name = "Akanksha"
city = 'Jaipur'
print(name)
print(type(name))
text = "Python"
print(text[0])      # First character
print(text.upper()) # Convert to uppercase

# #####4. Boolean (bool)
# A Boolean data type stores only two values:
# True
# False
# # Syntax :variable_name = True
# # eatures
# # Used in conditions and decision making
# # Important for if, while, and logical operations
is_passed = True
is_raining = False

print(is_passed)
print(type(is_passed))


# ####5. List (list)

# # A list is an ordered and mutable collection of items.
# # Syntax:list_name = [item1, item2, item3]
# # Features
# # Ordered
# # Mutable (can be changed)
# # Allows duplicate values
# fruits = ["apple", "banana", "mango"]
# print(fruits)
# print(type(fruits))
# # Operations on List
# numbers = [1, 2, 3]
# numbers.append(4)
# print(numbers)
# numbers.remove(2)
# print(numbers)


# # 6. Tuple (tuple)
# # A tuple is an ordered but immutable collection of items.
# # Syntax :tuple_name = (item1, item2, item3)
# # Features
# # Ordered
# # Immutable (cannot be modified)
# # Faster than lists
# # Allows duplicate values
# # Example
# colors = ("red", "green", "blue")

# print(colors)
# print(type(colors))

# # 7. Set (set)
# # A set is an unordered collection of unique items.
# # Syntax :set_name = {item1, item2, item3}
# # Features
# # Unordered
# # No duplicate values allowed
# # Mutable
# # Example
# numbers = {1, 2, 3, 4}
# print(numbers)
# print(type(numbers))
# # Set Operations
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.union(b))
# print(a.intersection(b))

# 8. Dictionary (dict)
# A dictionary stores data in key-value pairs.
# Syntax :dict_name = {
#     key1: value1,
#     key2: value2}
# Features
# Stores data in key-value form
# Mutable
# Keys must be unique
# Example
# student = {"name": "Akanksha","age": 20,"course": "AI & ML"}
# print(student)
# print(type(student))
# #  Adding New Data
# student["city"] = "Jaipur"
# print(student)

# # QUESTION222

# # Python Program to Demonstrate Dynamic Typing and type() Function

# # Integer
# a = 10

# # Float
# b = 3.14

# # String
# c = "Akanksha"

# # Boolean
# d = True

# # List
# e = [1, 2, 3, 4]

# # Tuple
# f = (10, 20, 30)

# # Set
# g = {1, 2, 3}

# # Dictionary
# h = {"name": "Akanksha", "course": "AI & ML"}

# # Printing values and their data types
# print("Value of a:", a)
# print("Data Type of a:", type(a))

# print("\nValue of b:", b)
# print("Data Type of b:", type(b))

# print("\nValue of c:", c)
# print("Data Type of c:", type(c))

# print("\nValue of d:", d)
# print("Data Type of d:", type(d))

# print("\nValue of e:", e)
# print("Data Type of e:", type(e))

# print("\nValue of f:", f)
# print("Data Type of f:", type(f))

# print("\nValue of g:", g)
# print("Data Type of g:", type(g))

# print("\nValue of h:", h)
# print("Data Type of h:", type(h))
# # Demonstrating Dynamic Typing
# x = 100
# print("\nValue of x:", x)
# print("Data Type of x:", type(x))

# x = "Python Programming"
# print("\nNow Value of x:", x)
# print("Now Data Type of x:", type(x))


3
# mutable data type
# list is mutable data type
# lst=[10,20,30]
# print(lst)

# #string are immutable
# name = "Python"

# # name[0] = "J"    Error

# new_name = "J" + name[1:]

# print(new_name)


#4
#list operations
# lst=[1,2,3,4,5]
# print(lst)
# lst.append(6)
# print(lst)
# lst.remove(2)
# print(lst[0:4])

# # #tuple indexing
# tup=(10,20,30,40,50)
# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[3])
# print(tup[4])

# #set operations
sat={1,2,3,4,5}
print(sat)
sat.union({6,7})
print(sat)
sat.intersection({2,3,4})
print(sat)
# #dictionary keys
student={"name":"Akanksha","age":21,"course":"Data Science"}
print(student["name"])
print(student["age"])
print(student["course"])
student.keys()
print(student.keys())
student.values()
print(student.values())
student.items()
print(student.items())


5
min student management system
student={
    "name": "Akanksha",
    "roll_no":111,
    "course": "B.Tech AIML"
}
#store marks using list
student["marks"] = [85, 90, 78]
#calculate average marks
total=sum(student["marks"])
#calculate average
average=total/len(student["marks"])
print("Student Name:", student["name"])
print("Roll No:", student["roll_no"])
print("Course:", student["course"])
print("Marks:", student["marks"])
print("Average Marks:", average)
