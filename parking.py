#%%
a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
d=int(input("enter the value of d"))
N=int(input("enter the value of N"))
lane1=[]
lane2=set()

for i in range(1,N+1):
    lane1.append(b+i*a)
    lane2.add(d+i*c)

for j in range(len(lane1)):
    if lane1[j] in lane2:
        print(f"same numbers:{lane1[j]}")    
print(lane1)
print(lane2)
# %%
