import random

naam = input("Wat is uw naam: ")

pogingen = 8

print(f"Welkom, {naam}, bij het spel galgje!")
moeilijkheidsgraad = input("Kies de moeilijkheidsgraad: makkelijk, gemiddeld of moeilijk: ")
print(f"Veel plezier met het spelen van galgje, je krijgt {pogingen} keer de kans om het juiste woord te raden!")

# ik maak gebruik van files openen. 3 aparte files met elk 20 woorden (dus in totaal 60 woorden) de 20 woorden zijn in elke file een stuk moeilijker
if moeilijkheidsgraad == "makkelijk":
    with open("galgjemoeilijk.txt") as file:
        woorden = file.readlines()
elif moeilijkheidsgraad == "gemiddeld":
    with open("galgjegemiddeld.txt") as file:
        woorden = file.readlines()
elif moeilijkheidsgraad == "moeilijk":
    with open("galgjemoeilijk.txt") as file:
        woorden = file.readlines()


woord = random.choice(woorden).strip()

geraden_letters = []      # een lege list aanmaken waar de geraden letters in komen te staan
pogingen_incorrect = 0

while pogingen_incorrect < pogingen:
    beeldscherm_woord = [letter if letter in geraden_letters else "_" for letter in woord]
    print("Woord: ", " ".join(beeldscherm_woord))
    print()

    if "_" not in beeldscherm_woord:
        print(f"Goed gedaan {naam}, je hebt het woord '{woord}' geraden!")
        print()
        break

    gok = input("Raad een letter: ")

    if gok in geraden_letters:
        print(f"Je hebt de letter '{gok}' al geraden.")

    if gok in woord:
        print("Goed bezig! Je komt steeds dichterbij het woord...")
        geraden_letters.append(gok)
        print()
    else:
        print(f"Jammer, de letter '{gok}' zit niet in het woord.")
        pogingen_incorrect += 1
        print()

    print(f"Je hebt nog {pogingen - pogingen_incorrect} pogingen over om het juiste woord te raden.")

if pogingen_incorrect == pogingen:
    print(f"Game over, het juiste woord was: '{woord}'.")

print("Dankjewel voor het spelen!")
