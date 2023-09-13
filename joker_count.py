#%%
cards_no=[]
no_of_card=int(input ("enter the total card u have"))
for i in range(no_of_card):
    q=str(input ("enter the number"))
    cards_no.append(q)

cards_no.sort()
k=1
for i in range(no_of_card):
    if cards_no[i] !="0":
        k=cards_no.pop(i)
        break

print(k+"".join(cards_no))   
    
    
    
    
 # %%
