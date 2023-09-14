#%%
N=6
I=3
X=2
def steps(N,I,X,count=0):
    i=I+1
    kk=0
    while i!=N:
        if kk==0:
            i+=X
            kk+=1
        else:
            i+=1
    count+=1
    X-=1
    if X>=0:
        return steps(N,I,X,count)
    else:
        return count
    
            
print(steps(N,I,X))
        
    
# %%
