#%%

import random as rd
from zipfile import ZIP_BZIP2
wordList = ["aegypti", "albimanus", "quadrimaculatus", "quinqefaciatus", "taenorychus", "tarsalis"]
wordPick = rd.choice(wordList)
#%%
#%%
answer = []
for _ in range(len(wordPick)):
    answer += "_"
#%%
LoseCond = False
wincount = 0
losecount = 0
LoseScore = 4
print(len(answer))
#%%
while(not LoseCond):

    
    UserWord = input("Enter your letter: ").lower()
    for L in range(0, len(wordPick)):
        if(UserWord == wordPick[L]):
            answer[L] = UserWord

    if(UserWord in answer):
        wincount+=1
        print(f"you answered correctly {wincount} times so far!")
        print(answer)
        if(not "_" in answer):
            print("YOUR A WINNER !! ")
            LoseCond = True
        

        
    else:
        losecount+=1
        print(f"{UserWord} is not part of the answer....")
        if((LoseScore - losecount) > 1):
            print(f"you have {LoseScore - losecount} wrong answers left......")
        if((LoseScore - losecount) < 1): 
            print(f"you have used all of your wrong answers....")
        if((LoseScore - losecount) == 1):
            print(f"you have {LoseScore - losecount} wrong answer left......")
        
    if(losecount >= LoseScore):
        LoseCond = True
        print(f"the answer was {wordPick}, you lose.")
    


# for x in wordPick:
#     if(x == UserWord):
#         print("true")
#     else:
#         print("false")