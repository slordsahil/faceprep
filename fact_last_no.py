#%%
def fact(n):
    if n <=1:
        return 1
    else:
        return n*fact(n-1)

sol=fact(int(input("enter the numer for factorial")))
# sol=str(sol)
for i in str(sol)[::-1]:
    if i!="0":
        print(i)
        break
    
# %%
