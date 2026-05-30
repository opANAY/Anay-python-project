cost_price=int(input("enter the cost price:  "))
selling_price=int(input("enter the selling price:  "))
loss=cost_price-selling_price
profit=selling_price-cost_price
if cost_price > selling_price:
    print("You got a loss of: ",loss)
else:
    print("You got a profit of: ",profit)
