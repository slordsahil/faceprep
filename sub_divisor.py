#%%
N=int(input("enter the number for play"))
count=0
while N!=0:
    if N==1:
        count+=1
        break
    for i in range(N//2,0,-1):
        if i==1:
            N-=1
            count+=1
            break
        if N%i == 0:
            N-=i
            count+=1
            break
    
        
print(count)
        
        
# %%
