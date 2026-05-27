amount=int(input("enter your amount: "))
print("The amount is: ",amount)
notes_500=amount//500
print(f"The number of 500 rupees notes in {amount} is {notes_500}")
notes_100=(amount%500)//100
print(f"The number of 100 rupees notes in {amount} is {notes_100}")