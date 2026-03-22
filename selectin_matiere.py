# Ce programme permet de sélectionner des matières à étudier au hasard

import random

print("""
Bonjour et bienvenue dans ce programme de sélection de matières à étudier au hasard.
En cas d'indécision, ce programme vous aidera à choisir l'ordre des matières à étudier.
Entrez les matières que vous voulez étudier aujourd'hui, tapez 'done' quand vous avez fini :
""")

matieres = []
while True:
    matiere = input("Entrez une matière (ou 'done' pour terminer) : ")
    if matiere.lower() == 'done':
        break
    if matiere in matieres:
        print("Cette matière est déjà dans la liste !")
    else:
        matieres.append(matiere)
        print(f"✓ '{matiere}' ajoutée.")

if not matieres:
    print("Vous n'avez entré aucune matière !")
else:
    print("\nVoici l'ordre des matières à étudier aujourd'hui :")
    random.shuffle(matieres)
    for i, matiere in enumerate(matieres, 1):
        print(f"{i}. {matiere}")
        
input("\nAppuyez sur Entrée pour quitter...")