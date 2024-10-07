import random

willekeurig_getal = random.randint(1, 100)      # random getal wordt gekozen tussen de 1 en 100


aantal_pogingen = int(8)

print(f"Ik heb een getal tussen de 1 en 100 gekozen. Probeer het getal te raden. Je krijgt {aantal_pogingen} keer de kans.")
for poging in range(1, aantal_pogingen + 1):      # hier gebruik ik range voor de pogingen die bij elkaar worden opgeteld
    gok = int(input(f"poging {poging}: Raad het getal: "))

    if gok == willekeurig_getal:
        print(f"Goed gedaan, je hebt het getal {willekeurig_getal} geraden in {poging} pogingen.")
        break           #als het getal in 1 keer is geraden dan is het spel hier klaar dus stopt de loop met break
    elif gok < willekeurig_getal:
        print("Het getal is hoger")     # bij een getal dat lager ligt dan de gekozen getal komt er op het beeldscherm te staan dat het getal hoger ligt
    else:
        print("Het getal is lager")     # dit geldt ook voor bij een te hoog geraden getal

    if poging == aantal_pogingen:
        print(f"Je pogingen zijn op. Het juiste getal was {willekeurig_getal}.")   # en tot slot: op=op bij pogingen, dus game over
print()
print("Einde spel")






