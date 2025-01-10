#Angelo Flores 1.06.25
#Initialize
import random
wins=0


losses=0

ties=0

#Functions
def game():
    1== "rock"
2== "paper"
3== "scissors"
print("Welcome to Rock Paper Scissors")
while True:
#Step 1: Player selects an option
    print("""Please select Rock, Paper, or Scissors to play""")
    object=input("Which one did you pick: ?")
    if object=="rock":
        print("Player chose rock")
    elif object=="paper":
        print("Player has chosen paper")
    elif object=="scissors":
        print("Player became scissors")
    #Step 2: Computer making a selection
    computer=random.randint(1,3)
    if computer==1:
        computer= "rock"
        print("Computer chose rock")
    elif computer==2:
        computer="paper"
        print("Computer chose paper")
    elif computer==3:
        computer= "scissors"
        print("Computer chose scissors")
    #Step 3: Outcome
    if object=="rock" and computer=="rock":
        print("Game ends in a tie")
        ties=ties+1
    elif object=="rock" and computer=="paper":
        print("Computer wins")
        losses=losses+1
    elif object=="rock" and computer=="scissors":
        print("Player has won")
        wins=wins+1
    if object=="paper" and computer=="rock":
        print("Player has won")
        wins=wins+1
    elif object=="paper" and computer=="paper":
        print("Game ends in a tie")
        ties=ties+1
    elif object=="paper" and computer=="scissors":
        print("Computer won")
        losses=losses+1
    if object=="scissors" and computer=="rock":
        print("Computer won")
        losses=losses+1
    elif object=="scissors" and computer=="paper":
        print("Player has won")
        wins=wins+1
    elif object=="scissors" and computer=="scissors":
        print("Game is tied")
        ties=ties+1
    print("Total wins= " +str(wins)+", total ties= "+str(ties)+ ", and total losses "+str(losses))
   #Step 4: Asking player to play again
    response=input("Play again y/n?")
    if response=="no":
        print("Thanks for playing")
        break


#Main
game()
