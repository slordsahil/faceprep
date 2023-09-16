#%%
string="ab5c7de96"
dicts={'1':1, '2':2, '3':3, '4':4,'5':5, '6':6, '7':7,'8':8, '9':9}
index_no=[]
digit=[]
stack=[]
string_len=len(string)
for i in range(string_len):
    if string[i] in dicts:
        index_no.append(i)
        digit.append(string[i])
    else:
        stack.append(string[i])
print(string)
print(digit)
print(stack)
print(index_no)
stringss=''
for i in range(string_len):
    if i==index_no[0]:
        index_no.pop(0)
        stringss+=digit.pop(0)
    else:
        stringss+=stack.pop()
print(stringss)
    
    
     
# %%
