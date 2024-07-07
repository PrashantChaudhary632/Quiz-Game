#Taking name as input and greeting the player
def greeting():
    import time
    timestamp = int(time.strftime("%H"))
    candidate = input("Enter your Name: ")
    if (timestamp > 0 and timestamp < 3 ):
        print("Hii!! ",candidate)
    elif(timestamp >= 3 and timestamp <12):
        print("Heyy!! ",candidate, " Good morning ")
    elif(timestamp >= 12 and timestamp < 15):
        print("Heyy!! ",candidate, " Good Afternoon")
    elif(timestamp >= 15 and timestamp < 18):
        print("Heyy!! ",candidate, " Good Evening")
    else:
        print("Hii!! ",candidate)  

    return candidate