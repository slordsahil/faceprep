#%%

r1=int(input("enter the rate of plastic bottle"))
r2=int(input("enter the rate of glass bottle(it must be higher than plastic bottle)"))

r3=int(input("enter the rate of glass bottle return money"))
money=int(input("enter the money u have to  buy bottle"))
count=0
while money>=r1 or money>=r2:
    if money ==0:
        break
    if r1<r2-r3 :
        if money>=r1:
            count+=1
            money-=r1
    elif r1>r2-r3:
        if money>=r2:
            count+=1
            money-=r2
            money+=r3
        elif money>=r1:
            count+=1
            money-=r1
print(count)
            
            
        
    
# %%
