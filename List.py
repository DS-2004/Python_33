L = ["apple","banana","kiwi","apple"]
print(L)
print(type(L))
print(L[0:])
print(L.copy())
L.append("cherry")
print(L)
#L.clear()
print(L)
L.count("a")
print(L)
h = ["watermelon","Mango"]
L.extend(h)
print(L)
x = L.index("apple")
print(x)
L.insert(1,"DragonFruit")
print(L)
L.pop(3)
print(L)
L.reverse()
print(L)
L.remove("kiwi")
print(L)
L.sort()
print(L)