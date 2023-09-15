#%%
N=int(input("enter the number for play"))
count=0
while N!=0:
    if N==1:
        count+=1
        break
    for i in range(2,N+1):
        if i==N:
            N-=1
            count+=1
            break
        if N%i == 0:
            a=N//2
            N-=a
            count+=1
            break
        
print(count)
        
        
# %%
