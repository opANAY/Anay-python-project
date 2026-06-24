print("enter marks obtained in 5 subjects")
mark1=int(input())
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())
total=mark1+mark2+mark3+mark4+mark5
print("total")
average= int(total/5)
print("average")
validRange=range(0,101)
if average not in validRange:
    print("invalid marks")
elif average in range(91,101):
    print("grade A1") 
elif average in range(81,91):
     print("grade A2")  
elif average in range(71,81):
    print("grade B1")
elif average in range(61,71):
    print("grade B2")
elif average in range(51,61):
    print("grade C1")
elif average in range(41,51):
    print("grade C2")
elif average in range(31,41):
    print("grade D1")
elif average in range(21,31):
    print("grade D2")
elif average in range(11,21):
    print("grade E")
elif average in range(0,11):
    print("grade F")

