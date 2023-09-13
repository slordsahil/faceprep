#%%
cards_no=[]
no_of_card=int(input ("enter the total card u have"))
for i in range(no_of_card):
    q=str(input ("enter the number"))
    cards_no.append(q)

cards_no.sort()

for i in range(no_of_card):
    if cards_no[i] !="0":
        cards_no[i-1],cards_no[i] =cards_no[i],cards_no[i-1]
        break

print("".join(cards_no))  
# %%
