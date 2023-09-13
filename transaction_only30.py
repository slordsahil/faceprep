#%%
def success_or_not(N):
    wallet=0
    for i in N:  
        if i==30:
            wallet+=30 
        else:
            if i-30>wallet:
                return "unsuccessful"
            else:
                wallet-=i-30
                wallet+=30 
    return "successful"
# n=int(input("total customers"))
# a=[]
# for  i in range(n):
#     a.append(int(input(f"enter customer no.{i+1} money")))
a=(input("enter customers money seperated by space"))
b=a.split(" ")
print(success_or_not(list(map(int, b))))
# %%
