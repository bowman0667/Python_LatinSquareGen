#%%
import random as rd

InputRawNames = input("enter any amount of names seperated by a comma: ")

IteratOverNames = InputRawNames.split(",")


print(f"It is{IteratOverNames[rd.randint(0, len(IteratOverNames))]}")

#%%
row1 = ['⏹','⏹','⏹']
row2 = ['⏹', '⏹', '⏹']
row3 = ['⏹', '⏹', '⏹']
#print(f"{row1}\n{row2}\n{row3}")

placeIcon = '💣'

placeIndex = input("Where wwould you like to place the bomb?")

MasterList = [row1, row2, row3]

rowIndex = int(placeIndex[0])
columnIndex = int(placeIndex[1])
MasterList[rowIndex-1][columnIndex-1] = placeIcon
print(f"{row1}\n{row2}\n{row3}")

#%%
playerChoice = input("pick a number from 1 - 10")
computerChoice = rd.randint(1, 10)
if(computerChoice > int(playerChoice)):
    print(f"The computer chose {computerChoice} and you chose {playerChoice}\nthe computer chose higher, you lose.")
elif(computerChoice == int(playerChoice)):
    print("Your lucky day, it's a draw. ")
else:
    print(f"The computer chose {computerChoice} and you chose {playerChoice}\nyou chose higher, you win!")

#%%
listone = [1,2,3,4,5]
print(len(listone))

