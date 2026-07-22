string=input("Enter a word : ")
print(string)
string2=("")
for i in string:
    string2=i+string2
print(f"original string is : {string}")
print(f"reverse word is : {string2}")