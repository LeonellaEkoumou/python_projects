# configure a rock paper scissor

name=input('Enter your name for start:  ')

print('Welcome', name,"nice to meet you!")

print("""
This is a rock scissor paper gamer!
You will play against me, Cain algoritmne 
But since now we are friend so just call me Cain 
""")

#ask to the user if they know the rules

ready=input('Before starting the game, have you ever play rock scissor paper before? [Yes or NO]:  ')
if ready=='Yes' or ready=='yes' or ready=='YES':
    print("Wonderful ! so we can directly start the match !")
elif ready=='no'or ready=='No' or ready=='NO':
    print("Hm....So let'start with a quick tutorial" )
else :
    print('Please verifie your input') # ADD A LOOP 
    while ready!='yes'or ready!='Yes'or ready!='YES' or ready!='No'or ready!='NO'or ready!='no':
     ready=input('have you ever play rock scissor paper before? [Yes or NO]:  ')

#In th case the user need a tutorial
if ready=='no'or ready=='No' or ready=='NO':
  print("""

This is how it works:
- You choose Rock, Paper, or Scissors.
- I choose too.
- Then we see who wins:

   Rock smashes Scissors
   Scissors cut Paper
   Paper covers Rock

If we both pick the same thing, it’s a tie....

Fine, seems like we are ready to start now !
""")
  
#Ask to the user if they want to work or left

want_play=input('Now do you want to play against me? [Yes/Exit]:  ')
if want_play=='Yes' or want_play=='yes' or want_play=='YES':
    print("Let's start the match !")
elif want_play=='exit' or want_play=='EXIT' or want_play=='Exit':
    print("Goodbye!")
    exit()

#START THE GAME

import random
options = ["rock", "paper", "scissors"]

while True:
    # player choice
    player = input("Choose rock, paper, or scissors: ").lower()

    # computer choice
    computer = random.choice(options)
    print("Computer chose:", computer)

    # decide winner
    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") \
         or (player == "scissors" and computer == "paper") \
         or (player == "paper" and computer == "rock"):
        print("You win!")
    else:
        print("You lose!")

    # ask if player wants to continue
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
       print("Thanks for playing! Goodbye!")
       break
