#%%
input=input("enter the input:\n")
input=input+"!"
total=0
count=1
for i in range(len(input)-1):
    if input[i]==input[i+1]:
        count+=1
    
    else:
        if count%2==0:
            total+=count
        count=1
print(total)
    
# %%
