# importing libraries
import time
import random
# declaring variables that will detect the user's target
target = ["gem", "files", "gold"]
encrypted_passwords = ["Golf Echo Mike",
"Foxtrot India Lima Echo Sierra", "Golf Oscar Lima Delta"]
# defining function that leaves seconds between each message
def print_pause (text):
    print(text)
    time.sleep(1.5)
# definig game functions that respond to user depending on his/her choices
def first_q():
    print_pause("Enter 1 to open the door\nEnter 2 to pull the brick")
def second_q():
    print_pause("Enter 1 to fire the candle with the match")
    print("Enter 2 to open the speaker")
def third_question():
    print_pause("Enter 1 to go up\nEnter 2 to pull the rope")
def open_door ():
    print("The door is Closed !!!")
def open_with_key ():
    print("You opened the door")
def pull_brick ():
    print("You found a key behind the brick")
def pulled_brick ():
    print("you dont need sth from  here again")
def fired_candled ():
    print("you fired the candle and now you can see better than before")
def open_speaker():
    print("The speaker made noise and you've been caught\n[GAME OVER]")
def taken_matches ():
    print("you don't need to come here again!!")
def up_stairs ():
    print_pause("you went up and you found a lock with a password")
    print("Enter 1 to try to open the lock\nEnter 2 to knock the door")
def pull_rope ():
    print("After you'd pulled the rope, a big rock fall on you and YOU DIED")
    print("[GAME OVER]")
def correct_pwd (x, y):
    print("You entered the correct password")
    print("\""+x+"\" was the encryption for the word\""+y+"\" and you found it")
def wrong_pwd_2 ():
    print("You entered wrong password the alarm rang and you've been caught")
    print("[GAME OVER]")
def wrong_pwd (trying):
    print("Wrong password, Please try again," +str(trying)+" TRIES LEFT")
def knock_door ():
    print("You knocked the door and have been caught\n[GAME OVER]")


# declaring variables that contains all used questions in the game
ask = "what do you want to do? 1/2: "
ask_s = "The password is : "
invalid = "Invalid, what do you want to do?: "
ans = "yes"

# defining a function that shows the user's score after each choice
def score_state (z):
    print("YOUR SCORE IS "+str(z))


# The main game loop
while ans == "yes":
    # declaring the items list which will be filled during the game
    items =[]

    # setting the score with 0 at the start of the game
    score = 0

    # setting number of tries, if the user consumed all of them he'll lose
    tries = 2

    # setting the target by using random
    g_target = random.choice(target)

    # matching the password with the target
    if g_target == "gem":
        g_encryption = encrypted_passwords[0]
    elif g_target == "files":
        g_encryption = encrypted_passwords[1]
    elif g_target == "gold":
        g_encryption = encrypted_passwords[2]


    # describe what's happening
    print_pause("You found your self in a dark house")
    print_pause("there's a low light from the next house you have only a candle")
    print_pause("The target is to find an unknown target being un-noticed")
    print_pause("you are in the living room and can see nothing")
    print_pause("but you see a room next to you but it closed")
    print_pause("also there is a brick in the wall seems to be broken")
    # show the user the valid options
    first_q()
    # take the first answer from the user
    answer = input(ask)
    # check if answer is valid or not
    while answer not in ["1", "2"]:
        print("Invalid")
        first_q()
        answer = input(invalid)

    # making conditions to the game
    while answer == "1":
        open_door()
        first_q()
        answer = input(ask)
        while answer not in ["1", "2"]:
            print("Invalid")
            first_q()
            answer = input(invalid)
    if answer == "2":
        pull_brick()
    # adding key to the list of items
        items.append("key")
    # showing score to the user
        score += 50
        score_state(score)
    if "key" in items :
        first_q()
        answer = input(ask)
        while answer not in ["1","2"]:
            print("Invalid")
            first_q()
            answer = input(invalid)

    # confirm that the user can't do the same sth twice
        while answer == "2":
            pulled_brick()
            first_q()
            answer = input(ask)
            while answer not in ["1", "2"]:
                print("Invalid")
                first_q()
                answer = input(invalid)
        if answer == "1":
            open_with_key()
    # updating score and showing it to the user
            score += 10
            score_state(score)
    time.sleep(1.5)

    # describe what happened according to user's input
    print_pause("you are in the room there is a desk in it")
    print_pause("you found a match sticks box")
    print_pause("also there is a speaker on the desk")
    second_q()
    answer = input(ask)
    # check if answer is valid or not
    while answer not in ["1", "2"]:
        print("Invalid")
        second_q()
        answer = input(invalid)

    # conditions of the game
    if answer == "1":
        fired_candled()
        while answer not in ["1", "2"]:
            print("Invalid")
            second_q()
            answer = input(invalid)
    elif answer == "2":
        open_speaker()
    # updating score and showing it to the user
        score -= 10
        score_state(score)
        time.sleep(1.5)

    # Ask user if he/she wants to play again after he/she losed
        quest = input("wanna play again? : ")
    # check if answer is valid or not
        while quest not in ["yes", "no"]:
            quest = input("Invalid, please try again")
        if quest == "yes":
            continue
        elif quest == "no":
            break
    time.sleep(1.5)

    # describe what happened according to the user's input
    print_pause("You got back to the living, now you can see stairs")
    print_pause("You can see also a sticky note on the wall which says : ")
    print_pause("remember me ---> "+g_encryption)
    print_pause("There is a rope hanging from the ceiling.")
    third_question()
    # taking input from the user
    answer = input(ask)

    # check if answer is valid or not
    while answer not in ["1", "2"]:
        print("Invalid")
        third_question()
        answer = input(invalid)

    # conditions of the game
    if answer == "1":
        up_stairs()
        score_state(score)
        answer = input(ask)
        while answer not in ["1", "2"]:
            print("Invalid")
            third_question()
            answer = input(invalid)
        if answer == "1":
            print_pause("Enter ur password")
            answer = input(ask_s)
            while answer != g_target and tries > 0:
                wrong_pwd(tries)
                tries -= 1
    # updating score and showing it to the user
                score -= 10
                score_state(score)
                answer = input(ask_s)
            if answer != g_target:
                wrong_pwd_2()
    # updating score and showing it to the user
                score -= 10
                score_state(score)
                time.sleep(1.5)
                quest = input("wanna play again? : ")
                while quest not in ["yes", "no"]:
                    quest = input("Invalid, please try again")
                if quest == "yes":
                    continue
                elif quest == "no":
                    break
            elif answer == g_target:
                correct_pwd(g_encryption, g_target)
    # updating score and showing it to the user
                score += 50
                print("YOU WON !!")
                score_state(score)
                time.sleep(1.5)

    # Ask the user if he/she wants to play again after he/she won
                quest = input("wanna play again? : ")
                while quest not in ["yes", "no"]:
                    quest = input("Invalid, please try again")
                if quest == "yes":
                    continue
                elif quest == "no":
                    break

    # rest of the conditions
        elif answer == "2":
            knock_door()
    # updating score and showing it to the user
            score -= 10
            score_state(score)
            time.sleep(1.5)
            quest = input("wanna play again? : ")
            while quest not in ["yes", "no"]:
                quest = input("Invalid, please try again")
            if quest == "yes":
                continue
            elif quest == "no":
                break
    elif answer == "2":
        pull_rope()
    # updating score and showing it to the user
        score -= 20
        score_state(score)
        time.sleep(1.5)

    # Ask the user if he/she wants to play again after he/she losed
        quest = input("wanna play again?: ")
        while quest not in ["yes", "No"]:
            quest = input("Invalid, please try again")
        if quest == "yes":
            continue
        elif quest == "no":
            break