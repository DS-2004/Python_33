a = 9
b = 3

#Arithmetic operation
print(a//b)
print(a**b)
print(a+b)
print(a-b)
print(a%b)
print(a/b)
print(a*b)

#Assignment Operators
a +=b
a -=b
a *=b
a /=b
a %=b
a //=b
a**=b

#Comparison Operators
if(a==b):
    print("a",a)
if(a!=b):
    print("a",a)
if(a>=b):
    print("a",a)
if(a<=b):
    print("a",a)
if(a>b):
    print("a ",a)
if(a<b):
    print("b ",b)

#Logical Operators
if(a and b):
    print("Hello")
if(a or b):
    print("Diksha")
a = True
print(not b)

#Identity Operators
x = ["mango","apple"]
y = ["chiku","apple"]
print(x is y)
print(x is not y)

#Membership Operators
for i in range(3,6):
    print(i)

#Bitwise Operators

print("a & b =",a & b)

print("a | b =",a | b)

print("a ^ b =",a ^ b)

print(" ~ b =", ~ b)

print("b>> =",b>>1)   #Bitwise right shift

print("a<< =",a<<1)   #Bitwise left shift



