f1 = open("demo.txt","w")
# print(f1.write("Hello Welcome to my world\n"))
print(f1.read("My name is Diksha"))
print("file is created")

f2 = open("demo2.txt","w")
print(f2.write("Hello Welcome to my world\n"))
print(f2.write("My name is Diksha"))
print(f2.write("I stay in kolhapur\n"))
print(f2.write("My friend stays in kalamba\n"))

f2 = open("demo.txt",'r')
print(f2.read(17))

f2 = open("demo2.txt","r")
print(f2.read())

f2 = open("demo2.txt","r")
line = f2.readline()
print("Read single line")
print(line)

f2 = open("demo2.txt","r")
line = f2.readlines()
print("Read single line")
print(line)

f2=open("demo.txt","a")
f2.write("Appending this line to the file\n")
print("Dataa appended to file")

seek()
f2 = open("demo2.txt",'r')
f2.seek(5)


tell()
f2 = open("demo2.txt",'r')
print(f2.tell())

f2 = open("demo2.txt","r+")
f2.write("Good morning")
f2.seek(15)

