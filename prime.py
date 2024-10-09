count = 0
def P(a,b):
    PList =[]
    global count
    for i in range(a,b):
        if i==0 and i==1:
         continue
        else:
           for j in range(2,int(i/2+1)):
             if i%j==0:
              break
             else:
                PList.append(i)
                count += 1
    return PList
a = int(input("Enter the number "))
b = int(input("Enter the number "))
lst = P(a, b)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)
    print("The count of Prime number is ",count)