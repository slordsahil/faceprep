#%%
num=str(input("enter the value of num"))


final=[]
num_list=list(num)
arr=[]
for i in range(10):
    arr.append(int(input("enter arr element")))
for i in range(len(num_list)):
    k=int(num_list[i])
    if k<arr[k]:
        num_list[i]=str(arr[k])
print("".join(num_list))
# %%
