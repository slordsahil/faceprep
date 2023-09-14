#%%
N=6
K=2
arr=[1,1,1,2,2,1]
count=0
uniq=[]
for i in range(N):
    if arr[i] not in uniq:
        uniq.append(arr[i])
        if len(uniq) == K:
            break
        count+=1
    else:
        count+=1
print(count)
            
                
            
        
# %%
