#this is a coding challenge from the 100 days of python 
#bootcamp
#%%
print("Pizza Menu")
order = input("Enter your size of pizza (S, M, or L): ")
addOns = input("do you want pepperoni? ")
addonsToppings = input("do you want extra cheese? ")
bill = float()
if(order == "S"):
    bill += 15
    if(addOns == "yes"):
        bill += 2
    else:
        bill += 0
    if(addonsToppings == "yes"):
        bill += 1
elif(order == "M"):
    if(addOns == "yes"):
        bill += 23
    else:
        bill += 20
    if(addonsToppings == "yes"):
        bill += 1
elif(order == "L"):
    if(addOns == "yes"):
        bill += 25
    else:
        bill += 20
    if(addonsToppings == "yes"):
        bill += 1
bill = format(bill, "0.2f")
print(f"Your final bill is {bill}$")

