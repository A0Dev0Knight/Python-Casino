import random

SAVE_FILE = "./saveData"
CHOICES = "🍒🍋💀"
OPTIONS = ("AGAIN" , "QUIT")

wallet = 0
proceed = 1

while(proceed):
    print("Enter deposit")
    wallet = input()

    for i in range(0, len(CHOICES)):
        print(random.choice(CHOICES), end="")

    print()
    print(f"Your balance is: {wallet}.")

    print()
    for i in range(0,len(OPTIONS)):
        print(OPTIONS[i])