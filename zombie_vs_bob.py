#%%
b=int(input("energy of bob"))
n=int(input("number of zombies"))
def zombie(b,n):
    for i in range(n):
        k=int(input("zombies energy"))
        if b<k:
            return "no"
        else:
            b-=(k%2)+(k/2)
    return "yes"
zombie_bob = zombie(b,n)
print(zombie_bob)

    
    
# %%
