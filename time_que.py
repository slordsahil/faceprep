#%%
h=int(input("enter hour"))
m=int(input("enter min"))

if m==0:
    h=24-h
else:
    h=23-h
    m=60-m
if h>0:
    print(f"{h:02}::{m:02}")
else:
    print(f"{h:03}::{m:02}")
    
# %%