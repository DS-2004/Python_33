a = int(input("Enter the value for a= "))
b = int(input("Enter the value for b= "))
c = int(input("Enter the value for c= "))

if(a>b and a>c):
    print("A =",a ,"is largest number among 3")
elif(b>a and b>c):
    print("B =",b ,"is largest number among 3")
else:
    print("C =",c,"is the largest among 3")

if(a<b and a<c):
    print("A =",a,"is the smallest among 3")
elif(b<a and b<c):
    print("B =",b,"is the smallest among 3")
else:
    print("C =",c,"is the smallest among 3")
