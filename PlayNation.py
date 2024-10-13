import tkinter as tk
from tkinter import ttk
import random
import os


# Functie voor het spel 'Raad het Nummer'
class RaadHetNummer(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pogingen = 8
        self.willekeurig_getal = random.randint(1, 100)

        self.label = tk.Label(self, text="Raad het nummer tussen 1 en 100:", font=("Arial", 16))
        self.label.pack(pady=10)

        self.entry = tk.Entry(self, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.result_label = tk.Label(self, text="", font=("Arial", 14), fg="blue")
        self.result_label.pack(pady=10)

        self.button = tk.Button(self, text="Raad", command=self.raad_nummer, font=("Arial", 12), bg="lightblue")
        self.button.pack(pady=10)

        self.pogingen_label = tk.Label(self, text=f"Pogingen over: {self.pogingen}", font=("Arial", 14))
        self.pogingen_label.pack(pady=10)

    def raad_nummer(self):
        try:
            gok = int(self.entry.get())
            if gok == self.willekeurig_getal:
                self.result_label.config(text=f"Goed gedaan! Het nummer was {self.willekeurig_getal}.", fg="green")
                self.button.config(state='disabled')
            elif gok < self.willekeurig_getal:
                self.result_label.config(text="Het nummer is hoger.", fg="blue")
            else:
                self.result_label.config(text="Het nummer is lager.", fg="blue")

            self.pogingen -= 1
            if self.pogingen == 0:
                self.result_label.config(text=f"Game over! Het juiste nummer was {self.willekeurig_getal}.", fg="red")
                self.button.config(state='disabled')
            self.pogingen_label.config(text=f"Pogingen over: {self.pogingen}")
        except ValueError:
            self.result_label.config(text="Vul een geldig nummer in.", fg="red")


# Functie voor het spel 'Galgje' met moeilijkheidsgraden
class Galgje(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pogingen = 8
        self.geraden_letters = []
        self.woord = ""

        self.label = tk.Label(self, text="Welkom bij Galgje!", font=("Arial", 16))
        self.label.pack(pady=10)

        # Moeilijkheidsgraad kiezen
        self.moeilijkheidsgraad_label = tk.Label(self, text="Kies de moeilijkheidsgraad:", font=("Arial", 14))
        self.moeilijkheidsgraad_label.pack(pady=5)

        self.moeilijkheidsgraad = ttk.Combobox(self, values=["makkelijk", "gemiddeld", "moeilijk"], font=("Arial", 12))
        self.moeilijkheidsgraad.pack(pady=10)

        self.start_button = tk.Button(self, text="Start Spel", command=self.start_galgje, font=("Arial", 12),
                                      bg="lightgreen")
        self.start_button.pack(pady=10)

        self.woord_label = tk.Label(self, text="_", font=("Arial", 18))
        self.woord_label.pack(pady=10)

        self.result_label = tk.Label(self, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.entry = tk.Entry(self, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.button = tk.Button(self, text="Raad de letter", command=self.raad_letter, font=("Arial", 12),
                                bg="lightblue", state="disabled")
        self.button.pack(pady=10)

        self.pogingen_label = tk.Label(self, text=f"Pogingen over: {self.pogingen}", font=("Arial", 14))
        self.pogingen_label.pack(pady=10)

    # Functie om het spel te starten
    def start_galgje(self):
        moeilijkheidsgraad = self.moeilijkheidsgraad.get()

        # Bestand kiezen op basis van moeilijkheidsgraad
        if moeilijkheidsgraad == "makkelijk":
            bestandsnaam = "galgjemakkelijk.txt"
        elif moeilijkheidsgraad == "gemiddeld":
            bestandsnaam = "galgjegemiddeld.txt"
        elif moeilijkheidsgraad == "moeilijk":
            bestandsnaam = "galgjemoeilijk.txt"
        else:
            self.result_label.config(text="Kies een geldige moeilijkheidsgraad", fg="red")
            return

        if os.path.exists(bestandsnaam):
            with open(bestandsnaam) as file:
                woorden = file.readlines()
            self.woord = random.choice(woorden).strip()
            self.geraden_letters = []
            self.pogingen = 8
            self.update_woord_label()
            self.button.config(state="normal")
            self.start_button.config(state="disabled")
            self.result_label.config(text="")
            self.pogingen_label.config(text=f"Pogingen over: {self.pogingen}")
        else:
            self.result_label.config(text=f"Kan bestand {bestandsnaam} niet vinden.", fg="red")

    # Update het label van het woord met geraden letters
    def update_woord_label(self):
        beeldscherm_woord = [letter if letter in self.geraden_letters else "_" for letter in self.woord]
        self.woord_label.config(text=" ".join(beeldscherm_woord))

    # Functie voor het raden van een letter
    def raad_letter(self):
        letter = self.entry.get().lower()
        if len(letter) == 1 and letter.isalpha():
            if letter in self.geraden_letters:
                self.result_label.config(text=f"Je hebt de letter '{letter}' al geraden.", fg="orange")
            elif letter in self.woord:
                self.geraden_letters.append(letter)
                self.result_label.config(text=f"Goed bezig! De letter '{letter}' zit in het woord.", fg="green")
            else:
                self.pogingen -= 1
                self.result_label.config(text=f"Jammer! De letter '{letter}' zit niet in het woord.", fg="red")

            self.pogingen_label.config(text=f"Pogingen over: {self.pogingen}")
            self.update_woord_label()
            self.entry.delete(0, tk.END)

            if "_" not in self.woord_label.cget("text"):
                self.result_label.config(text=f"Gefeliciteerd! Je hebt het woord '{self.woord}' geraden.", fg="green")
                self.button.config(state="disabled")

            if self.pogingen == 0:
                self.result_label.config(text=f"Game over! Het woord was '{self.woord}'.", fg="red")
                self.button.config(state="disabled")
        else:
            self.result_label.config(text="Voer een geldige letter in.", fg="red")


# Functie voor het starttabblad met 'PlayNation'
class StartScherm(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="PlayNation", font=("Arial", 48, "bold"), fg="blue")
        self.label.pack(pady=100)

        self.instructies = tk.Label(self, text="Welkom bij PlayNation! Kies een spel hierboven.", font=("Arial", 24))
        self.instructies.pack(pady=20)


# Hoofdprogramma met drie tabbladen (voor de startpagina en de twee spellen)
class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PlayNation")
        self.geometry("600x500")

        # Zet de achtergrondkleur
        self.configure(bg='lightblue')

        tab_control = ttk.Notebook(self)

        start_tab = StartScherm(tab_control)
        tab1 = RaadHetNummer(tab_control)
        tab2 = Galgje(tab_control)

        tab_control.add(start_tab, text="PlayNation")
        tab_control.add(tab1, text="Raad het Nummer")
        tab_control.add(tab2, text="Galgje")

        tab_control.pack(expand=1, fill="both")


# Start de applicatie
if __name__ == "__main__":
    app = GameApp()
    app.mainloop()
