import random

choice = ["Rock","Paper","Scissors"]
ro = 1
p1w = 0
p2w = 0
try:
    p1 = input("Player 1, choose your name: ")
except:
    ValueError
try:
    p2 = input("Player 2, choose your name, or to play with the computer, enter PC: ")
except:
    ValueError
while True:
    p1_vibor = input(f"{p1}: Rock, paper or scissors? ").capitalize()
    if p1_vibor not in choice:
        print("Invalid value entered, please enter: rock, scissors or paper.")
        continue
    if p2 == "PK":
        p2_vibor = random.choice(choice)
    else:
        p2_vibor = input(f"{p2}: Rock, paper or scissors? ").capitalize()
        if p2_vibor not in choice:
            print("Invalid value entered, please enter: rock, scissors or paper.")
            continue
    print(f"{p1} chose the {p1_vibor} and {p2} chose the {p2_vibor}")
    if p1_vibor == p2_vibor:
        result = "draw"
    elif (p1_vibor == "Rock" and p2_vibor == "Scissors") or (p1_vibor == "Paper" and p2_vibor == "Rock") or (p1_vibor == "Scissors" and p2_vibor == "Paper"):
        result = p1
        p1w += 1
    else:
        result = p2
        p2w += 1
    if result == "draw":
        print(f"Round {ro}: {result}")
        ro+=1
    else:
        print(f"Round {ro}: {result} got a point")
        ro+=1
    if p1w == 3:
        print(f"Player {p1} won")
        break
    elif p2w == 3:
        print(f"Player {p2} won")
        break