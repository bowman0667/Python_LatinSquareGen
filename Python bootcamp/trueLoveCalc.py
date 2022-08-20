#%%
name1 = input("what is your name? ")
name2 = input("what is your love interest's name? ")

name1 = name1.lower()
name2 = name2.lower()
combName = name1 + name2
score1 = 0
score2 = 0 
x = 0
y = 0 

x += combName.count("t")
x += combName.count("r")
x += combName.count("u")
x += combName.count("e")
y += combName.count("l")
y += combName.count("o")
y += combName.count("v")
y += combName.count("e")
print(f"your love score is {x}{y}")





