import tkinter as tk
from tkinter import messagebox
import random

# Functie om het Galgje spel te starten
def start_galgje():
    naam = naam_entry.get()

    if not naam:
        messagebox.showwarning("Fout", "Vul uw naam in!")
        return

    moeilijkheidsgraad = moeilijkheidsgraad_var.get()

    if moeilijkheidsgraad == "makkelijk":
        bestand = "galgjemakkelijk.txt"
    elif moeilijkheidsgraad == "gemiddeld":
        bestand = "galgjegemiddeld.txt"
    elif moeilijkheidsgraad == "moeilijk":
        bestand = "galgjemoeilijk.txt"
    else:
        messagebox.showwarning("Fout", "Selecteer een moeilijkheidsgraad!")
        return

    try:
        with open(bestand, 'r') as file:
            woorden = file.readlines()
    except FileNotFoundError:
        messagebox.showerror("Fout", f"Bestand {bestand} niet gevonden!")
        return

    woord = random.choice(woorden).strip()
    galgje_spel(naam, woord)

# Functie voor het spel zelf
def galgje_spel(naam, woord):
    geraden_letters = []
    pogingen = 8
    pogingen_incorrect = 0

    def raad_letter():
        nonlocal pogingen_incorrect
        gok = letter_entry.get().lower()

        if not gok or len(gok) != 1 or not gok.isalpha():
            messagebox.showwarning("Fout", "Voer één letter in (a-z)!")
            return

        if gok in geraden_letters:
            messagebox.showwarning("Fout", f"Je hebt de letter '{gok}' al geraden.")
            return

        if gok in woord:
            geraden_letters.append(gok)
            update_woord()
            if "_" not in beeldscherm_woord:
                messagebox.showinfo("Gewonnen", f"Goed gedaan, {naam}! Je hebt het woord '{woord}' geraden!")
                galgje_venster.destroy()
        else:
            pogingen_incorrect += 1
            pogingen_label.config(text=f"Je hebt nog {pogingen - pogingen_incorrect} pogingen over.")
            if pogingen_incorrect == pogingen:
                messagebox.showinfo("Verloren", f"Game over, {naam}. Het woord was '{woord}'.")
                galgje_venster.destroy()

        letter_entry.delete(0, tk.END)

    def update_woord():
        nonlocal beeldscherm_woord
        beeldscherm_woord = [letter if letter in geraden_letters else "_" for letter in woord]
        woord_label.config(text=" ".join(beeldscherm_woord))

    # Maak een nieuw venster voor Galgje
    galgje_venster = tk.Toplevel()
    galgje_venster.title("Galgje")

    tk.Label(galgje_venster, text=f"Welkom, {naam}, bij Galgje!", font=("Arial", 14)).pack(pady=10)

    beeldscherm_woord = ["_" for _ in woord]
    woord_label = tk.Label(galgje_venster, text=" ".join(beeldscherm_woord), font=("Arial", 24))
    woord_label.pack(pady=10)

    pogingen_label = tk.Label(galgje_venster, text=f"Je hebt nog {pogingen - pogingen_incorrect} pogingen over.")
    pogingen_label.pack(pady=10)

    letter_entry = tk.Entry(galgje_venster, font=("Arial", 14))
    letter_entry.pack(pady=5)

    gok_button = tk.Button(galgje_venster, text="Raad", command=raad_letter, font=("Arial", 14))
    gok_button.pack(pady=5)

# Functie voor het spel "Raad het Nummer"
def start_raad_het_nummer():
    naam = naam_entry.get()

    if not naam:
        messagebox.showwarning("Fout", "Vul uw naam in!")
        return

    nummer_spel_venster = tk.Toplevel()
    nummer_spel_venster.title("Raad het Nummer")

    willekeurig_getal = random.randint(1, 100)
    pogingen = 8
    pogingen_over = pogingen

    def check_gok():
        nonlocal pogingen_over
        try:
            gok = int(gok_entry.get())
            if gok == willekeurig_getal:
                messagebox.showinfo("Gefeliciteerd!", f"Goed gedaan, {naam}! Je hebt het getal {willekeurig_getal} geraden.")
                nummer_spel_venster.destroy()
            elif gok < willekeurig_getal:
                result_label.config(text="Het getal is hoger.")
            else:
                result_label.config(text="Het getal is lager.")

            pogingen_over -= 1
            pogingen_label.config(text=f"Je hebt nog {pogingen_over} pogingen over.")

            if pogingen_over == 0:
                messagebox.showinfo("Game Over", f"Je pogingen zijn op. Het juiste getal was {willekeurig_getal}.")
                nummer_spel_venster.destroy()
        except ValueError:
            messagebox.showerror("Fout", "Voer een geldig getal in.")

    # GUI voor Raad het Nummer
    tk.Label(nummer_spel_venster, text=f"Welkom, {naam}! Ik heb een getal tussen de 1 en 100 gekozen.").pack(pady=10)
    tk.Label(nummer_spel_venster, text="Probeer het getal te raden.").pack(pady=10)

    gok_entry = tk.Entry(nummer_spel_venster)
    gok_entry.pack(pady=5)

    gok_button = tk.Button(nummer_spel_venster, text="Raad", command=check_gok, font=("Arial", 14))
    gok_button.pack(pady=5)

    result_label = tk.Label(nummer_spel_venster, text="")
    result_label.pack(pady=5)

    pogingen_label = tk.Label(nummer_spel_venster, text=f"Je hebt {pogingen} pogingen.")
    pogingen_label.pack(pady=10)

# Hoofdmenu van de appstore
def open_appstore():
    root = tk.Tk()
    root.title("PlayNation")

    # Naam invoer
    global naam_entry
    tk.Label(root, text="Voer uw naam in:", font=("Arial", 14)).pack(pady=10)
    naam_entry = tk.Entry(root, font=("Arial", 14))
    naam_entry.pack(pady=5)

    # Moeilijkheidsgraad selectie voor Galgje
    global moeilijkheidsgraad_var
    moeilijkheidsgraad_var = tk.StringVar(value="")

    tk.Label(root, text="Kies de moeilijkheidsgraad (voor Galgje):", font=("Arial", 14)).pack(pady=10)
    tk.Radiobutton(root, text="Makkelijk", variable=moeilijkheidsgraad_var, value="makkelijk", font=("Arial", 12)).pack()
    tk.Radiobutton(root, text="Gemiddeld", variable=moeilijkheidsgraad_var, value="gemiddeld", font=("Arial", 12)).pack()
    tk.Radiobutton(root, text="Moeilijk", variable=moeilijkheidsgraad_var, value="moeilijk", font=("Arial", 12)).pack()

    # Knoppen voor spelletjes
    tk.Label(root, text="Kies een spel:", font=("Arial", 16)).pack(pady=20)

    btn_galgje = tk.Button(root, text="Speel Galgje", command=start_galgje, width=25, font=("Arial", 14))
    btn_galgje.pack(pady=10)

    btn_nummer = tk.Button(root, text="Speel Raad het Nummer", command=start_raad_het_nummer, width=25, font=("Arial", 14))
    btn_nummer.pack(pady=10)

    btn_afsluiten = tk.Button(root, text="Afsluiten", command=root.quit, width=25, font=("Arial", 14))
    btn_afsluiten.pack(pady=10)

    root.mainloop()

# Start de GUI appstore
open_appstore()
