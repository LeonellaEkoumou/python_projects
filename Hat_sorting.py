# harry potter sorting hat

print("The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four   Houses each first-year student goes to:🦁 Gryffindor,🦅 Ravenclaw,🦡 Hufflepuff or🐍 Slytherin")

print("Let's answer some questions for helping the hat to figure out which house suit for you !")
#Question1  If answer is 1 add 1 point to Gryffindor and Ravenlaw, if answer is 2 add 1 point to Hufflepuff and Slytherin
print('Q1) Do you like Dawn or Dusk?')
answer1 = int(input('Enter your answer (1-2): '))
if answer1 != 1 and answer1 != 2:
    while answer1 != 1 and answer1 != 2:
        print('Invalid answer. Please enter 1 for Dawn or 2 for Dusk.')
        answer1 = int(input('Enter your answer (1-2): '))
#Answer1 add points based on the user's choice
if answer1 == 1:
    gryffindor_points = 1
    ravenclaw_points = 1
    hufflepuff_points = 0
    slytherin_points = 0
elif answer1 == 2:
    gryffindor_points = 0
    ravenclaw_points = 0
    hufflepuff_points = 1
    slytherin_points = 1
print('Q2) When I’m dead, I want people to remember me as:')
print('1) The Good 2) The Great  3) The Wise 4) The Bold')
answer2 = int(input('Enter your answer (1-4): '))
if answer2 != 1 and answer2 != 2 and answer2 != 3 and answer2 != 4:
    while answer2 < 1 or answer2 > 4:
        print('Invalid answer. Please enter a number between 1 and 4.')
        answer2 = int(input('Enter your answer (1-4): '))
#Answer2 add points based on the user's choise
if answer2==1:
    gryffindor_points +=2
    ravenclaw_points +=0
    hufflepuff_points +=0
    slytherin_points +=0
elif answer2==2:
    gryffindor_points +=0
    ravenclaw_points +=2
    hufflepuff_points +=0
    slytherin_points +=0
elif answer2==3:
    gryffindor_points +=0
    ravenclaw_points +=0
    hufflepuff_points +=2
    slytherin_points +=0
elif answer2==4:
    gryffindor_points +=0
    ravenclaw_points +=0
    hufflepuff_points +=0
    slytherin_points +=2
print('Q3) Which kind of instrument most pleases your ear?')
print("1) The violin 2) The trumpet 3) The piano 4) The drum")
answer3= int(input('Enter your answer (1-4): '))
if answer3 != 1 and answer3 != 2 and answer3 != 3 and answer3 != 4:
    while answer3 < 1 or answer3 > 4:
        print('Invalid answer. Please enter a number between 1 and 4.')
        answer3 = int(input('Enter your answer (1-4): '))
#Answer3 add points based on the user's choise
if answer3==1:
    gryffindor_points +=4
    ravenclaw_points +=0
    hufflepuff_points +=0
    slytherin_points +=0
elif answer3==2:
    gryffindor_points +=0
    ravenclaw_points +=4
    hufflepuff_points +=0
    slytherin_points +=0
elif answer3==3:
    gryffindor_points +=0
    ravenclaw_points +=0
    hufflepuff_points +=4
    slytherin_points +=0
elif answer3==4:
    gryffindor_points +=0
    ravenclaw_points +=0
    hufflepuff_points +=0
    slytherin_points +=4
# Calculate the total score
total_score = answer1 + answer2 + answer3
# Determine the house based on the total score
if gryffindor_points > ravenclaw_points and gryffindor_points > hufflepuff_points and gryffindor_points > slytherin_points:
    print('Congratulations! you are in Gryffindor!🦁') 
elif ravenclaw_points > gryffindor_points and ravenclaw_points > hufflepuff_points and ravenclaw_points > slytherin_points:
    print('Congratulations! you are in Ravenclaw!🦅') 
elif hufflepuff_points > gryffindor_points and hufflepuff_points > ravenclaw_points and hufflepuff_points > slytherin_points:
    print('Congratulations! you are in Hufflepuff!🦡') 
elif slytherin_points > gryffindor_points and slytherin_points > ravenclaw_points and slytherin_points > hufflepuff_points:
    print('Congratulations! you are in Slytherin!🐍') 
else:
    print("It seems like you can fit in more than one house! Let's figure out with your teacher which house is the best for you...")