import random

choices = ["rock", "paper", "scissors"]
player = input("Wähle rock, paper oder scissors: ").strip().lower()
computer = random.choice(choices)

if player not in choices:
    print("Ungültige Eingabe.")
elif player == computer:
    print(f"Computer wählt: {computer}\nUnentschieden!")
elif (player, computer) in [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]:
    print(f"Computer wählt: {computer}\nDu gewinnst!")
else:
    print(f"Computer wählt: {computer}\nComputer gewinnt!")
