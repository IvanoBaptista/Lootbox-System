import rewards
import random
# a = rewards.get_new_skin()
Legendary_type = 0
Epic_type = 0
Rare_type = 0
Common_type = 0



for x in range(5):
    a = rewards.get_new_skin()
    if a == 'LEGENDARY':
        Legendary_type += 1 
    elif a == 'EPIC': 
        Epic_type += 1
    elif a == 'RARE':
        Rare_type += 1
    elif a == 'COMMON':
        Common_type += 1 

if Common_type > 0:
    print(Common_type, "x common")
if Rare_type > 0:
    print(Rare_type, "x rare")
if Epic_type > 0:
    print(Epic_type , "x epic")
if Legendary_type > 0:
    print(Legendary_type, "x legendary")



    # if reward.get_new_skin() == 'LEGENDARY':
    #     print("You got a LEGENDARY skin!")