# Harry Potter Sorting Hat 🧙‍♂️✨
import time
import random

# Fonction pour afficher du texte avec effet "machine à écrire"
def typewriter(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

# Introduction
typewriter("🎩 The Sorting Hat is ready to decide your fate at Hogwarts...")
time.sleep(1)
typewriter("It will place you in one of the four Houses:")
typewriter("🦁 Gryffindor, 🦅 Ravenclaw, 🦡 Hufflepuff, or 🐍 Slytherin!\n")
time.sleep(1)

typewriter("Let's answer some magical questions to help the Hat decide...\n")

# Initialisation des points
gryffindor_points = 0
ravenclaw_points = 0
hufflepuff_points = 0
slytherin_points = 0

# Question 1
typewriter("Q1) Do you like Dawn or Dusk?")
typewriter("1) Dawn 🌅  2) Dusk 🌙")
answer1 = int(input("Enter your answer (1-2): "))
while answer1 not in [1, 2]:
    typewriter("⚠️ Invalid answer. Please enter 1 for Dawn or 2 for Dusk.")
    answer1 = int(input("Enter your answer (1-2): "))

if answer1 == 1:
    gryffindor_points += 1
    ravenclaw_points += 1
else:
    hufflepuff_points += 1
    slytherin_points += 1

# Question 2
typewriter("\nQ2) When I’m dead, I want people to remember me as:")
typewriter("1) The Good 😇  2) The Great 👑  3) The Wise 📚  4) The Bold 💪")
answer2 = int(input("Enter your answer (1-4): "))
while answer2 not in [1, 2, 3, 4]:
    typewriter("⚠️ Invalid answer. Please enter a number between 1 and 4.")
    answer2 = int(input("Enter your answer (1-4): "))

if answer2 == 1:
    gryffindor_points += 2
elif answer2 == 2:
    ravenclaw_points += 2
elif answer2 == 3:
    hufflepuff_points += 2
elif answer2 == 4:
    slytherin_points += 2

# Question 3
typewriter("\nQ3) Which kind of instrument most pleases your ear?")
typewriter("1) The violin 🎻  2) The trumpet 🎺  3) The piano 🎹  4) The drum 🥁")
answer3 = int(input("Enter your answer (1-4): "))
while answer3 not in [1, 2, 3, 4]:
    typewriter("⚠️ Invalid answer. Please enter a number between 1 and 4.")
    answer3 = int(input("Enter your answer (1-4): "))

if answer3 == 1:
    gryffindor_points += 4
elif answer3 == 2:
    ravenclaw_points += 4
elif answer3 == 3:
    hufflepuff_points += 4
elif answer3 == 4:
    slytherin_points += 4

# Effet dramatique avant le résultat
typewriter("\nThe Sorting Hat is thinking...", 0.1)
time.sleep(2)
for i in range(3):
    typewriter("...", 0.3)
    time.sleep(0.5)

# Détermination de la maison
if gryffindor_points > max(ravenclaw_points, hufflepuff_points, slytherin_points):
    typewriter("🎉 Congratulations! You are in Gryffindor! 🦁")
elif ravenclaw_points > max(gryffindor_points, hufflepuff_points, slytherin_points):
    typewriter("🎉 Congratulations! You are in Ravenclaw! 🦅")
elif hufflepuff_points > max(gryffindor_points, ravenclaw_points, slytherin_points):
    typewriter("🎉 Congratulations! You are in Hufflepuff! 🦡")
elif slytherin_points > max(gryffindor_points, ravenclaw_points, hufflepuff_points):
    typewriter("🎉 Congratulations! You are in Slytherin! 🐍")
else:
    typewriter("🤔 It seems like you could fit in more than one house... The professors will help you decide!")