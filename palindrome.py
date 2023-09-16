#%%
str1=input("enter the string to")
str1_len=len(str1)
palindrome=[]
for i in range(str1_len):
    sub_string=''
    sub_string+=str1[i]
    for j in range(i+1,str1_len):
        sub_string+=str1[j]
        if sub_string==sub_string[::-1]:
            palindrome.append(sub_string)
a=print(palindrome)

# %%
max((palindrome),key=len)

# %%

# %%
