#%%
N=int(input("enter the number  of humans"))
L=int(input("enter the number  of vaccine we can give each day"))
a=N//L
b=N%L
if b==0:
    print(a)
else:
    print(a+1)
# %%
