import random

SAVE_FILE = "./saveData"
CHOICES = "🍒🍋💀"

OPTIONS = ("AGAIN" , "QUIT")

wallet = 0
proceed = 1

while(proceed):
    bet = 0
    # i need to make an initial deposit of x RON for first round to work
    if wallet == 0:
        print("Enter initial deposit")
        wallet = int(input())

        print(f"\nYour balance is: {wallet}. How much do you wish to bet?")
        
        # place the bet
        bet = int(input())
        wallet -=bet

    else:
        print("Enter your bet")
        bet = int(input())
        wallet -=bet
    
    round = []
    var = 2
    for i in range(0, len(CHOICES)):
        machineChoice = random.choice(CHOICES)
        round.append(machineChoice)
        print(machineChoice, end="")
        if var > 0:
            print(" | ", end="")
            var -=1

    if round == "🍒🍒🍒":
        bet *= 4
        wallet += bet
        print(f"\nTripple cherry combo!")
    else:
        if round == "🍋🍋🍋":
            bet *= 2
            wallet += bet 
            print(f"\nWhen life gives you lemons, you make lemonade!")
        else:
            if "💀" in round:
                print(f"\n\"I came to myself in a dark wood, for the straight way was lost\" - Dante Alighieri")

    print(f"\nYour balance is: {wallet}.")

    if wallet == 0:
        proceed = 0
    else :
        if wallet < 0:
            print(f"\nYou owe me {-wallet} RON mate!")
            proceed = 0

    for i in range(0,len(OPTIONS)):
        print(f"\nPress {i} for\t{OPTIONS[i]}",end="")

    nextRound = input()

    if nextRound == 1:
        proceed = 0
