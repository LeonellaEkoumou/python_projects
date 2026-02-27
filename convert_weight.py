print("""
Welcome to the intergalactic weight conversion tool.

Since you attend to travel to another planet,
You have to know and carry your weight 
change by the other planet gravity.
""")

# Ask for the user's Earth's weight
print("First, enter your Earth's weight in kg")
weight = float(input(''))

print("""
Then we need to know the id number of your destination planet.
Remember :
1: Mercury, 2: Venus, 3: Mars, 4: Jupiter,
5: Saturn, 6: Uranus, 7: Neptune
""")
planet = int(input(''))


if planet == 1:
    destination_w = weight * 0.38
    print(destination_w, "kg")
elif planet == 2:
    destination_w = weight * 0.91
    print(destination_w, "kg")
elif planet == 3:
    destination_w = weight * 0.38
    print(destination_w, "kg")
elif planet == 4:
    destination_w = weight * 2.53
    print(destination_w, "kg")
elif planet == 5:
    destination_w = weight * 1.07
    print(destination_w, "kg")
elif planet == 6:
    destination_w = weight * 0.89
    print(destination_w, "kg")
elif planet == 7:
    destination_w = weight * 1.14
    print(destination_w, "kg")
else:
    print("Invalid number ❌")
