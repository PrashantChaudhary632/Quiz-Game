#greeting the player

import greet as g
candidate = g.greeting()  #receives the name of the player from greeting.py file

#take the input from user until the user press 'n'
import add_ques as a
while True:
    admin = input("Do you want to add questions?(y/n) : ")
    if(admin.lower()=='y'):
        a.adding_question()
    else:
        break

#game starts with the player permission
player = input("Do you want to play game??(y/n) : ")
if(player.lower()=='y'):
    import game_logic as g
    g.game_logic()
else:
    #prints the thankyou message 
    print(f"{candidate}, Thank you please do try to play next time ")




