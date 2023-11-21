name = input("Type your name: ")
print("Welcome", name, "to this adventure!")
answer = input("You have come to the end of the word, you can't go further, you can only go left or right. Which way would you like to go? ").lower()


if answer == "left":
     answer = input("You have come to a river. You can walk around it or swim across? Type walk to walk around and swim to swim across. ").lower()
    
     if answer == "swim":
       print("You swam across and wore eaten  by aligator.")   

     elif answer=="walk":
         print("You walked for many miles, ran out of water and you lost the game:(")
    
     else:
         print("Invalid Option!You lose")
    

elif answer == "right":
      answer = input("You have come to a bridge, it looks wobbly do you want to cross it or head back(cross/back)?: ").lower()
         
      if answer == "back":
        print("You go back and got lost and you lose the game.")

      elif answer== "cross":
          answer= input("You cross the bridge and meet a stranger. Do you talk to them?(yes/no): ").lower()
           
          if answer =="yes":
              print("You talk to stranger. They give you a ride and you reach to your destination. Hurray!! You won the game:)")

          elif answer=="no":
              print("You are left alone there with no food and transportation!You lose:(")

          else:
              print("Invalid Option. You lose!")


       
else: 
    print("Not a valid option.You lose.")


print("Thank you for trying", name,".")