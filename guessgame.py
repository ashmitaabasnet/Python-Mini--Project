import random
top_range = input("Enter a number: ")
if top_range.isdigit():
  top_range = int(top_range)

  if top_range <= 0:
      print("Please enter a number greater than 0 next time.")
      quit()
else:
 print("Type a number next time.")
 quit()
 
random_number= random.randint(0,top_range)
guess = 0
while True:
  guess += 1
  user_guess = input("Make a guess: ")
  if user_guess.isdigit():
   user_guess = int(user_guess)
  else:
   print(" Please Type a number next time.")
   continue
  if user_guess == random_number:
    print("you got it.")
    break
  elif user_guess > random_number:
    print("You were above the number!")
  else:
    print("You were below the number!")
print("You got the number")