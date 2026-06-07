# print("hello hii kese ho ") 
# # data types 
# # 0 data types 
# name = "upflairs"
# print(name)


# # print("type of variable 👉👉👉👉",type(name)) 


# str 
# list 
# tuple 
# dict 
# set 
# bool 
# complex 
# int 
# float 




#>>>>>>>>>>>>>>>>>>>>>> str 
name = "Diya"
# print("My Name is :- ",name)

# print("type of my variable : - ",type(name)) #### type funtion type check krne ke kam aata hai

# print("len of my string : - ",len(name)) 
# upper_case =name.upper()
# print("upper case :- ",upper_case)
# lower_Case =upper_case.lower()
# print("lower case :- ",lower_Case)


# lw =upper_case.casefold()

# print(lw)

# name = "RITIK"
# print(name.casefold()) task 2 
# name = "dev"
# print(name.title())
# print(name.capitalize()) Task 2 


company_name  = "upflairs"
# print(len(company_name))
# print(company_name.strip())


# intro = " hello hii kese ho" ### task 3 


# indexing and slicing 
company_name  = "upflairs"
# print(company_name[0])
# print(company_name[7])
# print(company_name[-1])

# print(company_name[0:3])
# company_name >>>> task 4  revrse the string 

# name = "Ritik "
# last_name = " kumar"

# print(name,last_name)   #### join
# print(name + " "+ last_name)


# str * str 
# name = "Dev"
# print(name * name)  #>>>>>>
# print(name + name)
# print(name + 2)
# print(name *  2)


# intro ="""Hey, I’m Ritik Kumawat — a passionate developer and Data Science enthusiast from Rajasthan.
# I work on Python, Machine Learning, Deep Learning,
# FastAPI, and Generative AI projects.
# I love building smart applications, exploring new tech,
# and turning ideas into real-world solutions. 🚀"""
# print(intro)

# intro.strip
# intro.split()

# intro ="hello my name is   \n govind "
# intro.split("\n", "")
# name = 'dev'
# name = "dev"   ### task 

# name = "Govind"
# address = "jaipur"
# print(f"my name is {name} and i from {address} ")
# path = r"C:\Users\kumaw\OneDrive\Desktop"
# print(path)


# input function 
# name =input("enter you name : -")
# print(name)
# print(type(name))

# number1  =int(input("enter you first number :- "))
# number2  =int(input("enter you second number :- "))

# print(number1+ number2)
# print(type(number1))
# print(type(number2))

# >>>>>>>>>>>> list >>>>>>>>



# lst =[1,2,3,5,2,5,"hello", 3.2]
# print("This is my first list :- ",lst)
# print("Len of my list :-",len(lst))
# print("Type of my list :- ",type(lst))


# print = 10 
# print(print)
# list = 10 
# print(">>><><<<<<",list)
# lst =[1,2,3,5,2,5,"hello", 3.2]
# print(lst[0])
# print(lst[3])
# print(lst[2])
# print(lst[4])
# print(lst[6])
# print(lst[7])

# print(lst[-1]
# )


# print(lst[0:5])
# print(lst[2:5])
# print(lst[2:7])




# operations 

# fruits = ["apple", "banana", "mango"] 
# add item
# fruits.append("orange") ####
# fruits.insert(0, "grapes")
# fruits.remove("apple")
# fruits.remove(2)
# fruits.pop()
# fruits.pop(1)
# fruits.clear()
# fruits.copy()
# print(fruits.count("apple"))
# print(fruits.index("apple"))
# fruits[0]="Kiwi"

# fruits.reverse()
# print("fruits list :- ",fruits)
# lst1 = [1,2,32]
# lst2 = [ 2,3,5]
# print(">>>>>>>",2 in lst2)
# print(lst1+lst2)
# | Function | Use             |
# | -------- | --------------- |
# | len()    | Length          |
# | max()    | Maximum value   |
# | min()    | Minimum value   |
# | sum()    | Sum of elements |
# | sorted() | Sort list       |
# 



#tuples
# tpl = (1,2,"hello",2.2,8)
# print(tpl)
# print("This is my first tuple :",tpl)
# print("The length of my tuple is :",len(tpl))
# print(tpl[0])
# print(tpl[0:4])

# a = 1,2,3,46,76,958,"hello"
# print(a)
# print(type(a))
# print(len(a))

# a ,b ,c = [1,2,3] ###tuple unpacking
# print(a)
# print(b)
# print(c)


# tpl =(1,24,47,"Akanksha",5.5,5,2,2,5,2)
# print(tpl)
# print(tpl.count(2)) #tell how many times the number occurs
# print(tpl.index("Akanksha")) ##tell the position of the the number given 

####type casting
# tpl = (1,2,275,49,335,"Akanksha")
# print(tpl)
# print(type(tpl))
# print("tuple convert into list")
# lst = list(tpl)
# print(">>>>>",lst)
# print(">>>>>",(type(lst)))
# lst.append(100) ##add 100 into list bcz in tuple changment is not allowed amd list can be changed 
# print(lst)
# print("list convert back into tuple")
# tpl = tuple(lst)
# print(tpl)

###dictionary
##mutable
##double values ko allow krti hai
##duplicate key is not allowed
##denoted by dict
# dict  = {"name" : "Akanksha","Roll no.": "2301", "Branch": "AIML" ,"Address": "Sikar"}
# print(dict)
##name,roll no,branch,address >>>>>keys
##akanksha,23aiml01,Aiml,sikar>>>>>values
##key+values == items

# print("dict keys",dict.keys())
# # print("dict values",dict.values())
# print("dict items",dict.items())

# print(dict["name"])
# print(dict["branch"])
# print(dict["subject"])

# print(dict)

# print(dict.get("name"))

# print(dict.pop( "Address"))
# print(dict.popitem())
# # dict.pop
# dict.popitem

# #####TASK :: update finction use karna hai 


###setdefault

# car ={"brand":"Ford","Model":"Mustang","year":"1984"}
# x = car.setdefault("color","White")

# print(x)

#####TASK 2 deep copy(important)

# car ={"brand":["Ford","Honda","hero"],"Model":"Mustang","year":"1984"}
# car['year'] =200
# print(car)
# for x in car.values():
#     print(x)
# for x in car.keys():
#     print(x)
#     for x in car.items():
#         print(x)


###SET 
#mutable
#unorderd collection

# a = {1,2,3,4,5}
# print("This is my set:",a)
# print("type of my set:",type(a))
# print("length of set:",a)

# set.remove("hello")
# print(a)
###remove function agr apne pas set mine elemnet na ho toh error de deta hai
# but ##discard function element dhundta hai set m milta hai toh theek otherwise koi error nhi dega esa ka esa print kr dega

# a.discard("Hello")
# print(a)


# ##Assignment 4

# ##In python ,data types defines the type of value a variable can store
# #### Variables can store data of different types, and different types can do different things.


# #1 INTEGER: An integer is a whole number without a decimal point.
# # It can be positive, negative, or zero. 
# # Syntax : variable_name = integer_value
# ##example:
# a = 10
# b = -25
# c = 0

# print(a)
# print(type(a))

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

# pi = 3.14
# temperature = -12.5

# print(pi)
# print(type(pi))
# ####3String (str)
# # A string is a sequence of characters enclosed in quotes.
# # Syntax :variable_name = "text"

# # Features
# # Used to store text
# # Immutable (cannot be changed directly)
# # Supports indexing and slicing

# name = "Akanksha"
# city = 'Jaipur'
# print(name)
# print(type(name))
# text = "Python"
# print(text[0])      # First character
# print(text.upper()) # Convert to uppercase

# #####4. Boolean (bool)
# # A Boolean data type stores only two values:
# # True
# # False
# # Syntax :variable_name = True
# # eatures
# # Used in conditions and decision making
# # Important for if, while, and logical operations
# is_passed = True
# is_raining = False

# print(is_passed)
# print(type(is_passed))


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

# # #set operations
# sat={1,2,3,4,5}
# print(sat)
# sat.union({6,7})
# print(sat)
# sat.intersection({2,3,4})
# print(sat)
# # #dictionary keys
# student={"name":"Akanksha","age":21,"course":"Data Science"}
# print(student["name"])
# print(student["age"])
# print(student["course"])
# student.keys()
# print(student.keys())
# student.values()
# print(student.values())
# student.items()
# print(student.items())


#5
#min student management system
# student={
#     "name": "Akanksha",
#     "roll_no":111,
#     "course": "B.Tech AIML"
# }
# #store marks using list
# student["marks"] = [85, 90, 78]
# #calculate average marks
# total=sum(student["marks"])
# #calculate average
# average=total/len(student["marks"])
# print("Student Name:", student["name"])
# print("Roll No:", student["roll_no"])
# print("Course:", student["course"])
# print("Marks:", student["marks"])
# print("Average Marks:", average)




















