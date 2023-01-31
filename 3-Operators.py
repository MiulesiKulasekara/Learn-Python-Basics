# Operators

# Assignment operator

name = "Miulesi"
age  = 22 
salary = 100000 + 2000 

# Arithmetic Operators

addition = 1 + 1 
substraction = 2 - 1 
multipication = 4 * 3
division = 6 / 3
modules = 8 % 5 
exponentiation = 3 ** 4 #( 3 * 3 * 3 * 3 )
floorDivision = 5 // 2 # round down to the nearest whole number

print(addition)
print(substraction)
print(multipication)
print(division)
print(modules)
print(exponentiation)
print(floorDivision)

a = 10
print(a) 

a += 1  # a = a + 1
print(a)
a -= 2  # a = a - 2
print(a)

a *= 3  # a = a * 3
print(a)

a /= 6  # a = a / 6
print(a)

a %= 2  # a = a % 2
print(a)

# Comparison Operators

# ==  equal
# != not equal
# > greater than
# < less than
# >= greater than or equal
# >= less than or equal

x = 10
y = 10

if(x == y):
    print("x equals y")
elif(x != y):
    print("x is not equal y")

m = 15
n = 31 

if( m > n):
    print("m is grater than n")
elif(m < n):
    print("m is less than n")
else:
    print("m is equals to n")

i = 5
j = 82

if( i >= j):
    print("i is grater than or equal j")
elif(i <= j):
    print("i is less than or equal j")

# Boolean Operators

condition1 = True
condition2 = False

# not condition1 ==> oppesite
# condition1 and condition2 ==> if all conditions are true it returns TRUE only
# condition1 or condition2 ==> if one of the condition is true it returns TRUE 

# Bitwise Operators

# OPERATOR	    DESCRIPTION	            SYNTAX
# &	            Bitwise AND	            x & y
# |	            Bitwise OR	            x | y
# ~	            Bitwise NOT	            ~x
# ^	            Bitwise XOR	            x ^ y
# >>	        Bitwise right shift	    x>>
# <<	        Bitwise left shift	    x<<

# Ternary Operator

#normal
def myAge1(age):
    if(age > 18):
        print("You are an adult")
    else:
        print("You are a child")

myAge1(22)

#ternary
def myAge2(age):
    print("You are an adult") if age > 18 else print("You are a child")
    #true condition   if part   else part    false condition
myAge2(21)