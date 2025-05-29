#Angelo Flores
#4th Period
#01/15/25
#Initialize
#These variables are variables that change depending on the player continues with game
import random
health=100

hunger=0

allies=0
day=1
bandage=0
food=0
npc=input("What is your name?")
#functions
#Outcomes presents different situations for the player to experience
def outcome():
    global food
    global bandage
    global health
    global hunger
    global allies
    global day
    global npc
    situations=random.randint(1,4)
    if situations==1:
        print("You were attacked by a zombie and lost health.")
        health=health-30
        print("Your health is now at "+str(health)+" health.")
        print("You fend off the zombie and find a bandage and food.")
        bandage=bandage+1
        food=food+1
        use=input("Use food?")
        aid=input("Use bandaid?")
        if use=="yes":
            print("Your hunger went down.")
            food=food-1
            hunger=hunger-20
        if aid=="yes":
            print("Your health went up.")
            health=health+30
    elif situations==2:
        print("Scavenging was successful and you found 3 food and 0 bandages.")
        food=food+3
        use=input("Use food?")
        if use=="yes":
            print("Your hunger went down.")
        elif use=="no":
            print("Your food was saved but your hunger went up.")
            hunger=hunger+20
            print("Your hunger level is now at "+str(hunger))
    elif situations==3:
        print("Scavenging was hard as "+npc+" was shot by raiders.")
        print(npc+" has lost health.")
        health=health-40
        print("Health is now at "+str(health))
    elif situations==4:
        print(npc+" has a new ally.")
        allies=allies+1
    if health<=0:
        print(npc+" has perished.")
        print("Total days survived= "+str(days)+" days. Total food= "+str(food) +". Total allies= "+str(allies))
    if hunger==100:
        print("Each day your hunger is full, you lose health.")
        health=health-50
#Rest is a function that allows the player to sleep, wasting a day, but regains health and increases hunger
def rest():
    global health
    global hunger
    print(npc +" slept today and gained health, but you have increased hunger.")
    health=health+30
    hunger=hunger+40
    print(npc+"'s health is now at "+str(health)+". But your hunger is now at "+str(hunger)+".")
    if hunger>=100:
        health=health-50
        print("Your hunger is high, scavenge and eat food.")
#Info is a function that displays the player's stats
def info():
    global health
    global hunger
    global allies
    global day
    global food
    global bandage
    print(npc+" is at day "+str(day)+", their health is at "+str(health)+", hunger is at "+str(hunger)+", and have "+str(allies)+ "allies.")
    print(npc+" has "+str(food)+" food items and "+str(bandage)+ " bandages lefts.")
#Game holds all of the game under 1 whole function
def game():
    print("""
    It is the year 2000.
    A virus has spread throughout the world and has wiped out 90% of the world's total population.
    You are one of the last survivors on Earth and must overcome the zombie outbreak.""")
while True:

    print("It is day "+str(day)+" and your health is at "+str(health)+" and your hunger is at "+str(hunger))
    print("""What would you like to do today?
        1.Scavenge
        2.rest
        3.display stats
        4.quit""")
    activity=int(input("What are you doing today?"))
    if activity==1:
        outcome()
    if activity==2:
        rest()
    if activity==3:
        info()
    if activity==4:
        print("Thanks for playing!")
        break
    day=day+1
    if day==100 and health>=50:
        print(npc+" was saved by a new acting government.")
        print(npc+" survived with "+str(health)+" health, "+str(hunger)+" hunger level, "+str(allies)+" allies.")
        again=input("Play again y/n?")
    elif day==100 and health<=50:
        print(npc+" was overwhelmed by zombies.")
        print("The end.")
        again=input("Try again?")
if again==no:
    print("Thanks for playing")
    break


#main
game()
