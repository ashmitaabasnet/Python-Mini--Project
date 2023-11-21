import random
user_score = 0
computer_score=0
 
options= ["rock","paper","scissors"]
while True:
    user_input = input("Chose Rock/Paper/Scissors or Q to Quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0,2)  
    #rock:0 paper:1, scissor:2q
    computer_pick = options[random_number]
    print("Computer picked ", computer_pick + ".")
    if (user_input == "rock" and computer_pick == "scissors") or \
       (user_input == "paper" and computer_pick == "rock") or \
       (user_input == "scissors" and computer_pick == "paper"):
        print("You won!")
        user_score += 1
    elif user_input == computer_pick:
        print("Its a tie")
    else:
        print("You lost")
        computer_score += 1
    break
print("You won", user_score, "times.")
print("Computer won", computer_score, "times.")
print("Goodbye!")

        



