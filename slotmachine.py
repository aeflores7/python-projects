#Angelo Flores
#init
import random
import time
characters=["♥","♦", '♠', '♣', '☆', '7',"♥","♦", '♠', '♣', '☆'] # Symbols for the slot; double characters= weighted characters
random.choices(characters, weights= [5,5,5,5,5,.1,5,5,5,5,5])
credits=100# the virtual currency of someone
#functions
def slots(): # Holds the whole slot machine code
    global credits
    print("""Welcome to global slotmachines.
      Here is where you can win big and lose small.
      Our current symbols: """+str(characters[0:6])+""".
      So the odds are tilted towards the customer currently.""")
    while True: # Loops the process of spinning the machine
        icon1=random.choice(characters)
        icon2=random.choice(characters)
        icon3=random.choice(characters)

        print("You currently have " +str(credits)+". It costs 10 credits to spin.")
        user=input("Would you like to spin? Y for yes. N for no.")
        if user=="y":
            credits=credits-10
            for i in range(3):
                print("spinning")
                time.sleep(2)
            print(icon1+icon2+icon3)
            if icon1=="7" and icon2=="7" and icon3=="7": # Displays when someone wins the biggest possible prize
                print("Congrats you won our BIGGEST jackpot. You now have 10000 credits.")
                credits=credits+10000
                print("You now have "+str(credits)+" in your account.")
            elif icon1==icon2 and icon1==icon3 and icon2==icon3: # Displays when someone matches 3 in a row
                print("You got a match. You win 500 credits.")
                credits=credits+500
                print("You now have "+str(credits)+" in your account.")
            else:
                print("Your credit balance is now at "+str(credits)+".")
                if credits==0: # Loops the slot machine as if someone was inserting more money after hitting 0
                    print("You have 0 credits. Go get more money")
                    time.sleep(2)
                    print("...")
                    credits=credits+100

                elif user=="n":# breaks the loop and lets the player leave
                    print("thanks for playing at the slot machine. Have a good night")
                    break
        elif user=="n":
            user=input("Would you like to quit? Y to quit N to continue")
            if user=="y":# breaks the loop and lets the player exit
                print("Thanks for playing")
                break



#1. Introduction
#2. Ask player if they want to spin or quit
#3. Randomly pull 3 symbols from our list (Make sure to remember the 3 symbols/ use a variable)
#4. Display the symbols
#5. determine the outcome (Jackpot, match, loss)(IF ELIF ELSE)
slots()
