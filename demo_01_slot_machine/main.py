import random

SAVE_FILE = "./saveData"
CHOICES = "🍒🍋💀"

OPTIONS = ("AGAIN" , "QUIT")

wallet = 0
proceed = 1

while(proceed):
    bet = 0
    # i need to make an initiaal deposit of x RON for it to work
    if wallet == 0:
        print("Enter initial deposit")
        wallet = int(input())

        print(f"\nYour balance is: {wallet}. How much do you wish to bet?")
        bet = int(input())
        wallet -=bet

    else:
        print("Enter your bet")
        bet = int(input())
        wallet -=bet
    
    round = []
    for i in range(0, len(CHOICES)):
        machineChoice = random.choice(CHOICES)
        print(machineChoice + " ", end="")

    print()
    print(f"Your balance is: {wallet}.")

    print()
    for i in range(0,len(OPTIONS)):
        print(OPTIONS[i])