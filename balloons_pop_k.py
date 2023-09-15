#%%
N=int(input("enter the total numbers of groups of balloon:\n"))
K=int(input("enter the numbers of groups of balloon he can destroy in each round:\n"))
arr=list(map(int,input("enter no. of balloon in each group seperated by space:\n").split()))
count=0
while len(arr) >=K:
    arr.sort(reverse=True)
    b=0
    i=0
    while b<K:

        arr[i]-=1
        if arr[i]==0:
            arr.pop(i)
            b+=1
        else:
            i+=1
            b+=1
    count+=1
print(count)
    


# %%
