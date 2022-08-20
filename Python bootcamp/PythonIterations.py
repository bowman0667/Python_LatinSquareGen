#%%
from selectors import EpollSelector


fruits = ["apple", 10, 1.23, "pear"]
for x in fruits:
    print(f"{x} pie")

#%%
#day 5 coding challenge, calculate avereage height from a list of heights
heights = input("enter a list of heights")
heights = heights.split()
y = 0
z = 0
aveDef = 0.0
for x in heights:
    y += 1
    z += float(x)
aveDef = z/y
print(round(aveDef, 2))



#calculate the highest score
#this line converts the list of strings into a list of integers
for i in range(0, len(heights)):
    heights[i] = int(heights[i])

startI = 0 
for value in range(0, len(heights)):
    if (heights[value] > startI):
        startI = heights[value]
        print(startI)
print(f"The highest value = {startI}")

#%%    
#using a for loop with the range funtion.
# range(x, y) excludes y includes x. The default is 
# a step of 1, but this can be changed with the 3rd parameter. 
total = 0 
for i in range(1, 101):
    total += i
print(total)
    
#%%
#calculate the sum of all even numbers from 1 to 100. 
evenTotal = 0 
for i in range(1, 101):
    if(i%2 == 0):
        evenTotal += i
print(evenTotal)
        
#%%
# the Fizzbuzz coding interview question
# print each number from 1 to 100, when a number is divisible by 3 print
# the word fizz instead of the number, when the number is divisible
# by 5 print the word buzz instead of the number, and if the number is 
# divisible by 15 print the word fizzbuzz instead of the number 

for i in range(1, 101):
    if(i%3 == 0):
        if(i%5 == 0):
            print("fizz-buzz")
        else:
            print("fizz")
    elif(i%5 == 0):
        if(i%3 == 0):
            print("fizz-buzz")
        else:
            print("buzz")
    else:
        print(i)



#%%
number = 0.75
for i in range(1, 5):
    number *= 0.75
print(number)
print(i)
#%%
for i in range(0, 5):
    print(i)
    
