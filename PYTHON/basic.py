# print("hello world")
# print("123hello")

# x = 10
# y = "Akanksha"
# print(x)
# print(y)


# x = y = z = "orange"
# print(x)
# print(y)
# print(z)

# a = "ABC"
# x = "A"
# y = "B"
# z = "C"

# print(x)
# print(y)
# print(z)

# #VARIABLE  --Variables are the containers of storing the data values
# # A variable name must start with a letter or the undrescore character 
# # A variable name cannot start with number
# # A variable name can only  contain alpha- numeric character and underscore (A-z, 0-9)


myvar ="Akanksha"
my_var = "Akanksha"
_my_var = "Akanksha"
myVar ="Akanksha"
MYVAR = "Akanksha"
myvar2 ="Akanksha"

# #print()pretty flexible you can enter muktiple value output

# print(34)
# print("salman khan")
# print("Akanksha",23,56.5,"true")
# print("Akanksha",56 ,"divya")

# print("hello khah se ho aap", end="")
# print("mein jaipur se hu")

# print("hello",end="-")
# print("world")

# print("hello");print("how are you");print("i'm ok")
# print(x,y,z)

# #dynamic typing ---c,c++ language you have tell the datatype before giving varible to 

# # int a = 20

# i = 56
# print(i)
# print(type(i))
# #dynamic binding == in pyhotn there is no fix data

# a = 45
# print(a)


# a = "Akanksha"
# print(a)

# a = int('5') #str ->int
# print(a)
# print(type(a))      #casting

# ##Many values to many varibles --pyhton allows you to assign values to multiple variables

# x,y,z = "apple","banana","orange"
# print(x)
# print(y)
# print(z)

# x=y=z= "orange"
# print(x)
# print(y)
# print(z)

# #unpack of collection --if ypu have a collection of values in a list,tuples etc.
# #python allow you to extract the values into varibales ,this is called unpacking
# #list unpacking

# a = ["apple","divya","juice"]
# x,y,z = a
# print(x)
# print(y)
# print(z)

# #tuple unpack
# x =(3,4,5,)
# a,b,c = x
# print(a,b,c)




# #string unpack
# name = "ABC"
# a,b,c = name
# print(a,b,c)

# x = "pyhton"
# y = "is"
# z = "good"
# print(x,y,z)
# print(x+y+z)

# #casting -- if you wnat to specify the data type of the variable ,this can be done with casting

# x = int(3)
# y = float(3.0)
# z = str(3)
# print(x)
# print(y)
# print(type(z))

# ##type casting  -- you can convert one data type to another data type 
# #1 .implicit type v=conversion


# print(6+5.8)
# print(type(6),type(5.8))

# #2 explicit type conversion -- internallly know the data type

# x = float(20)
# print(x)


#  ## user input -- 
#  # static VS dynamic software -- static don't talk with usre they only gives information (ex- calender ,blog ,clock)
#  ##dynamic --user input deta hai (ex--youtube,ola,zomato)
# # a = input("What is your name: ")
# # b = input("what is your age: ")
# # print(a)
# # print(b)

# # a= int(input("Enter first number: "))
# # b = int(input("Enter second number: "))

# # c = a+b
# # print(c)

# # name = input("aapka naam btao: ")
# # print("hello",name)

# # a = int(input("Enter first number: "))
# # b = int(input("Enter second number: "))

# # c = a*b
# # print("total= ",sum)

#  #swap two number program
# a = 20
# b = 12

# a,b = b,a 
# print("A: " ,a )
# print("B: ",b)

# a = 12
# b = 20
# c = 13 
# a,b,c = c,a,b

# print("A: ",a)
# print("B: ",b)
# print("C: ",c)
#  #string rule-

#  # #1 -sequence of characters inside the quotes
# #   include letter number and space
# # string are immuatable/unchanged
# # but we can manupualte the strins by using concatenation sliclin,formatting
# # delete an entire string variable (python not possible to delete individual)

# a ='hello'
# print(a)

# b ="python is good"
# print(b)

# c = '''hey how are you
# i'm ok '''
# print(c)

# import sys

# # Check if argument is provided
# if len(sys.argv) != 2:
#     print("Usage: python prime.py <number>")
#     sys.exit()

# # Convert command line argument into integer
# num = int(sys.argv[1])

# # Prime checking logic
# if num <= 1:
#     print(num, "is not a Prime Number")
# else:
#     is_prime = True

#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(num, "is a Prime Number")
#     else:
#         print(num, "is not a Prime Number")


#         # Integer Example
# a = 10
# b = 10

# print("Integer Comparison")
# print(a == b)   # Checks value
# print(a is b)   # Checks memory location


# # List Example
# x = [1, 2, 3]
# y = [1, 2, 3]

# print("\nList Comparison")
# print(x == y)   # Checks value
# print(x is y)   # Checks object identity


# # String Example
# s1 = "Python"
# s2 = "Python"

# print("\nString Comparison")
# print(s1 == s2)
# print(s1 is s2)
# name = "Diya"
# print(name)

# upper_case = name.upper()
# print(" upper case : ",upper_case)
# lower_case = upper_case.lower()
# print("lower case : ",lower_case)

# from os import name


# campany_name ="google"
# print(len(campany_name))
# print(campany_name.strip())

# #indexing and slicing
# name = "Akanksha"      
# print(name[0])  #A
# print(name[1])  #k              
# print(name[2])  #a
# print(name[3])  #n
# print(name[4])  #k
# print(name[5])  #s
# print(name[6])  #h
# print(name[7])  #a
# print(name[-1]) #a


# print(name[0:4])  #Akan
# print(name[4:])   #ksha

    

# name ="Akanksha"
# last_name = "jangir"
# full_name = name + " " + last_name
# print(full_name)

# # str+ str
# name="Akanksha"
# print(name*name)
# print(name+name)
# print(name+2)
# print(name*2)


# name = "Akanksha"
# place="Jaipur"
# print(f"my name is {name} and i am form {place}") 


# input function
# name = input("enter your name: ")
# print(name)
# print(type(name))
# num1 = int(input("enter first number: "))       
# num2 = int(input("enter second number: "))  
# print(num1 +num2)
# print(type(num1))
# print(type(num2))

# print("hello world")


# len("hello world")