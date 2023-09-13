#%%

final=[]
input_list=list(input("Enter the input string: "))
input_key=list(input("Enter the input strings key: "))
for i in range(len(input_key)):
    if input_key[i] in input_list:
        final.append(input_key[i])
        input_list.remove(input_key[i])
        while input_key[i] in input_list:
            final.append(input_key[i])
            input_list.remove(input_key[i])

print(final)
print(input_list)
            
          

            
            

# %%
