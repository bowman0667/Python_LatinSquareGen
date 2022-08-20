#%%
float(7%2)
#%%
ans = int(input())

if(ans % 4 == 0):
    if(ans % 100 == 0):
        if(ans % 400 == 0):
            print("Leap Year")
        else:
            print("Not Leap Year")
else:
    print("Def not a leap year")
        

