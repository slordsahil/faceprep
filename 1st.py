#%%
str1=input("enter the string")
dicts={'1':1, '2':2, '3':3, '4':4,'5':5, '6':6, '7':7,'8':8, '9':9}
b=[]
i=0
while i<len(str1):
    if j==len(str1)-1:
        break
    if str1[i] in dicts.keys():
        a=[]
        a.append(str1[i])
        for j in range(i+1, len(str1)):
            if str1[j] in dicts.keys():
                a.append(str1[j])
            else:
                break
        b.append(a)
        i=j
    else:
        i+=1

print(str1)
print(b)

total=0
for q in range(len(b)):
    total+=int("".join(b[q]))
print(total)
    
# %%
