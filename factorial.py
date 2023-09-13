#%%
n=int(input("numbers of pencils"))
m=int(input("numbers of erasers"))
p=int(input("mom said to take pencils"))
e=int(input("mom said to take erasers"))
def fac(n):
    a=1
    for i in range(1,n+1):
        a*=1
    
    return a

pencils=fac(n)/(fac(n-p)*fac(p))
erasers=fac(m)/(fac(m-e)*fac(e))
print(pencils*erasers)

# %%

# %%
