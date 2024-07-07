#greeting the player

import greet as g
candidate = g.greeting()


import add_ques as a
while True:
    admin = input("Do you want to add questions?(y/n) : ")
    if(admin.lower()=='y'):
        a.adding_question()
    else:
        break

player = input("Do you want to play game??(y/n) : ")
if(player.lower()=='y'):
    import game_logic as g
    g.game_logic()
else:
    print(f"{candidate}, Thank you please do try to play next time ")




