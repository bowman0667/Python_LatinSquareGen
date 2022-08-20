#%%
TrapList = input("Enter the code for any number of traps seperated by a space: ")

TrapList = TrapList.split()
print(TrapList)
iterIndex = len(TrapList)
# %%

#%%
#This just takes the first entry in the latin square and moves it to the next positon in the list, and shifts the rests of the entries to the right and takes the last entry and places it in the first spot. I loop though the user defined size of each transect I use this method in the logic below. 
for i in TrapList:
    TrapList[1] , TrapList[2], TrapList[3], TrapList[4], TrapList[0] =  TrapList[0], TrapList[1] , TrapList[2], TrapList[3], TrapList[4]
    print(TrapList)

#%%
print(range(0, len(TrapList)-1)) 

# %%
sizeChoice = int(input('''Enter the size of the latin square (you need to only enter one number ie.. "5" would be a 5x5 latin square. minumum size is 2, maximun size is 10:   '''))
# I am trying to find a more elegant way of making this generic so the user can pick any size latin square they want. This is my current solution. I do have to add the functionality of randomizing the first entry. 
if (sizeChoice == 2):
    TrapLayout = input("Enter the two trap codenames: ")
    TrapLayout = TrapLayout.split()
    for i in TrapLayout:
        TrapLayout[1], TrapLayout[0] = TrapLayout[0], TrapLayout[1]
        print(TrapLayout)
if (sizeChoice == 3):
    TrapLayout = input("Enter the two trap codenames: ")
    TrapLayout = TrapLayout.split()
    for i in TrapLayout:
        TrapLayout[1], TrapLayout[2], TrapLayout[0] = TrapLayout[0], TrapLayout[1], TrapLayout[2]
        print(TrapLayout)


#%%
# ignore this below, this is the start of the logic to randomize the first transect in the latin square. 
import random as rd
def ReturnTrapList(size, number_iterations):
    trapindexer = []
    for i in range(0, size):
        trapindexer.append(i)
    for j in range(0, number_iterations):
        rd.shuffle(trapindexer)
        print(trapindexer)

ReturnTrapList(2, 2)


