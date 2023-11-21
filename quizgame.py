print("Welcome to Quiz Game! ")
playing = input("Do you want to play a Computer quiz game: ")
if playing.lower() != "yes":
    quit()
print("Okay lets play the game :)")
score = 0
answer = input("What is the fullform of CPU? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Wrong")

answer = input("What is the fullform of GPU? ")
if answer.lower() == "graphic processing unit":
    print("Correct")
    score +=1
else:
    print("Wrong")

answer = input("What is the fullform of RAM? ")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("Wrong")

answer = input("What is the fullform of GIGO? ")
if answer.lower() == "garbage in garbage out":
    print("Correct")
    score += 1
else:
    print("Wrong")

print("Congratulations you have answered " + str(score) + " questions correct.")

