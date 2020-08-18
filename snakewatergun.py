import random
import pyfiglet
import os
gameoptions = ['s','w','g']
banner = pyfiglet.figlet_format("Snake Water Gun")
print(banner)
print("Code by 2kwattz")
username = input("Enter your name : ")
rounds = 0
userpoints = 0
compoints = 0
print(f"\nWelcome {username}... Let's Play \n\nTotal rounds : 10\nEnter s for Snake\nEnter w for Water\nEnter g for Gun\n")
while (rounds<10):
    comp = random.choice(gameoptions)
    rounds = rounds+1
    uservalue = input(":")
    if uservalue == 's' and comp == 's':
        print(f"{rounds} Round : {username} chose Snake.Computer chose snake\nIts a Draw")
        print(f"{username} Points : {userpoints} \t\t Computer points : {compoints}\n")

    elif uservalue == 's' and comp == 'w':
        userpoints = userpoints +1
        print(f"Round {rounds}. \n{username} chose Snake.Computer chose Water\n{username} Won this round")
        print(f"{username} Points : {userpoints} \t\t Computer points : {compoints}\n")

    elif uservalue == 's' and comp == 'g':
        compoints = compoints + 1
        print(f"Round : {rounds}. {username} chose Snake,Computer chose gun.\nComputer won this round")
        print(f"{username} Points : {userpoints} \t\t Computer points : {compoints}\n")
    elif uservalue == 'w' and comp == 'w':
        print(f"Round : {rounds}. {username} chose Water , Computer chose water\nIts a Draw")
        print(f"{username} Points : {userpoints} \t\t Computer points : {compoints}\n")
    elif uservalue == 'w' and comp == 's':
        compoints = compoints + 1
        print(f"Round : {rounds}. {username} chose Water , Computer chose Snake\nComputer won this round")
        print(f"{username} Points : {userpoints} \t\t Computer points : {compoints}\n")
    elif uservalue == 'w' and comp == 'g':
        userpoints = userpoints +1
        print(f"Round : {rounds}. {username} chose Water , Computer chose gun\n{username} won this round")
        print(f"{username} Points : {userpoints} \t\t Computer points : {compoints}\n")
    elif uservalue == 'g' and comp == 'g':
        print(f"Round : {rounds}. {username} chose Gun , Computer chose gun\nIts a draw")
        print(f"{username} Points : {userpoints} \t\t Computer points : {compoints}\n")
    elif uservalue == 'g' and comp == 'w':
        compoints = compoints + 1
        print(f"Round : {rounds}. {username} chose Gun, Computer chose Water\nComputer won this round")
        print(f"{username} Points : {userpoints} \t\t Computer points : {compoints}\n")
    elif uservalue == 'g' and comp == 's':
        userpoints = userpoints +1
        print(f"Round : {rounds}. {username} chose gun , Computer chose snake\n{username} won this round")
        print(f"{username} Points : {userpoints} \t\t Computer points : {compoints}\n")
    else:
        print("Incorrect parameters . You have to insert either 's' for Snake , 'w' for Water,'g' for Gun\n")
        break
    if rounds == 10:
        if userpoints > compoints:
            print("Congratulations ! You Won the game !")
        elif compoints > userpoints:
            print("Sorry . You Lose")
