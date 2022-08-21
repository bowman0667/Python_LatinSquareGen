#%%
import random as rd
wordList = ["aegypti", "albimanus", "quadrimaculatus", "quinqefaciatus", "taenorychus", "tarsalis"]
wordPick = rd.choice(wordList)
#%%

UserWord = input("Enter your letter: ").lower()

if(UserWord in wordPick):
    print("the letter is in the word")
else:
    print("the letter is not in the word")