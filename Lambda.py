A = "apple"

d = lambda string: string.upper()
print(d(A))
 
d = lambda string: string.capitalize()
print(d(A))

b = lambda string: string.replace("apple","MANGO")
print(b(A)) 

d = lambda string: string.lower()
print(d(A))


w = "Hello world   "

d = lambda string: string.strip()
print(d(w))

d = lambda string: string.casefold()
print(d(w))

d = lambda string: string.center(20)
print(d(w))




# cube = lambda x: x*x*x
# print(cube(5))

# avg = lambda x,y,z:(x+y+z)/3
# print(avg(49,89,23))

# sub = lambda x,y:(x-y)
# print(sub(3,1))

# mul = lambda x,y:(x*y)
# print(mul(32,12)) 

# div = lambda x,y:(x/y)
# print(div(12,34))

# mod = lambda x,y:(x%y)
# print(mod(34,56))

# flr = lambda x,y:(x//y)
# print(flr(23,56))

# exp = lambda x,y:(x**y)
# print(exp(34,56))



# def any(fx, value):
#     return 6 + fx(value)

# print(any(cube,3))

# def some(fx,value):
#     return 4 + fx(value)
# print(some(lambda x: x*x*x,3))