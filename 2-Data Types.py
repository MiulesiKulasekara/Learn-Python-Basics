# Data types

name = "Shamal" 
age = 22 
height = 1.3

print(type(name))   #<class 'str'>
print(type(age))    #<class 'int'>
print(type(height)) #<class 'float'>

print(isinstance(name , str)) #True
print(isinstance(name , int)) #False

# Python automatically detects the form of the variable type.
# So it automatically knows the datatype of the variable.

# But we can also create a variable of the spesific  type by using the class constructor.

a = 2
print(type(a))

a = float(2)
print(type(a))

# We can convert one data type to another by using the class construtor == CASTING

age = "20"

num = "20"
age = int(num)

print(type(age))