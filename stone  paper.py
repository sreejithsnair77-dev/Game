import random
choices = ["stone", "paper", "scissor"]
rules = {"stone": "scissor", "scissor": "paper", "paper": "stone"}
userchoice = input("Enter your choice (stone, paper, scissor): ").lower()

if userchoice not in choices:
    print("Invalid choice! Please choose stone, paper, or scissor.")
else:
    computerchoice = random.choice(choices)

    print(f"\nYour choice: {userchoice}")
    print(f"Computer's choice: {computerchoice}")
    if userchoice == computerchoice:
        print("Result: It's a draw!")
    elif rules[userchoice] == computerchoice:
        print("Result: You win!")
    else:
        print("Result: Computer wins!")
