#%%
# The instructor is calling these classes "modules" I have never heard
# this terminology before.
import random as rd
import My_module as mod
# random integer
rand_int = rd.randint(1, 10)
print(rand_int)
print(mod.pi)
# random float between 0 and 1. 
rand_float = rd.random()
print(rand_float)

#random float between 0 and 5. 
random_larger_float = rand_float * 5
print(random_larger_float)

#random number generator challenge
#%%
coinChoice = input("heads or tails? (H/T")
choicerInt = 0
coinfFlip = rd.randint(0,1)
if(coinChoice == "H" or coinChoice == "h"):
    choicerInt = 0
    longformchoice = "Heads"    
else:
    choicerInt = 1
    longformchoice = "Tails"

if(coinfFlip == choicerInt):
    print(f"The coinflip was {longformchoice}, you win!")
else:
    print(f"The coinflip was not {longformchoice}, you lose.")

