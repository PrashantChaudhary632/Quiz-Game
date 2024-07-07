def game_logic():

#Reads the data from the JSON file
    import json
    with  open("E:\\Python Examples\\quiz_data.json","r") as f:
            quiz_data = json.load(f)
    
    #Game starts with user permission
    yes_no = input("Let's Start?? Type y/n to continue: ")  
    bounty=0  #winning price, initial is 0
    if (yes_no.lower() == "y"):
        for k in range(len(quiz_data)):  #iterates all the question in lists
            print(k+1, quiz_data[k]["questions"])
            for i in range(4):
                print(i+1, quiz_data[k]["answers"][i])
            rightanswer = int(input("Enter your option: "))
            if rightanswer == quiz_data[k]["correctans"]:
                bounty += 5000 * (k + 1)
                print("You won ", bounty)
                continue    #iterates to next loop
            else:
                print("Sorry, you lost")
                print("Here is your remaining amount", bounty)
                break