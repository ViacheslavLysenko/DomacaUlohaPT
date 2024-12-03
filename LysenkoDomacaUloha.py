from tkinter import Tk, Label, Button, Entry, Toplevel
from PIL import Image, ImageTk
import random
import matplotlib.pyplot as plt
import sys
import os

# Funkcia na získanie správnej cesty k obrázkom v prípade .exe alebo pri spustení z kódu
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Funkcia na generovanie čísel a zobrazenie výsledkov
def open_new_window():
    try:
        # Získame hodnoty z textových polí
        num_min = int(entry_min.get())  # Minimálna hodnota
        num_max = int(entry_max.get())  # Maximálna hodnota
        multiplier = float(entry_multiplier.get())  # Hodnota násobku
    except ValueError:
        num_min = 0  # Prednastavená minimálna hodnota
        num_max = 100  # Prednastavená maximálna hodnota
        multiplier = 1  # Prednastavený násobok

    # Generovanie náhodných čísel
    numbers = [random.randint(num_min, num_max) for _ in range(12)]

    # Násobenie každého čísla zadaným násobkom
    multiplied_numbers = [int(num * multiplier) for num in numbers]  # Použitie int() na zaokrúhlenie na celé čísla

    # Odčítanie čísel medzi sebou
    differences = [multiplied_numbers[i] - multiplied_numbers[i + 1] for i in range(len(multiplied_numbers) - 1)]

    # Prirátanie 10 ku každému číslu
    adjusted_numbers = [num + 10 for num in multiplied_numbers]

    # Vytvorenie reťazca pre zobrazenie pôvodných čísel a rozdielov
    differences_with_numbers = [f'{multiplied_numbers[i]} - {multiplied_numbers[i + 1]} = {differences[i]}'
                                for i in range(len(differences))]

    # Vytvorenie nového okna pre zobrazenie výsledkov
    new_window = Toplevel(m)
    new_window.title("Výsledky")

    # Vypísanie výsledkov do nového okna
    result_label = Label(new_window, text=f'Pôvodné čísla: {", ".join(map(str, numbers))}\n'
                                         f'Násobené čísla: {", ".join(map(str, multiplied_numbers))}\n'
                                         f'Rozdiely:\n' + '\n'.join(differences_with_numbers))
    result_label.pack()

    # Vykreslenie grafu
    plt.plot(adjusted_numbers, marker='o')
    plt.title('Upravené hodnoty')
    plt.xlabel('Index')
    plt.ylabel('Hodnota')
    plt.grid()
    plt.show()


# Hlavné okno aplikácie
m = Tk()
m.minsize(width=600, height=600)
m.title("Lysenko_DomacaUloha")

# Načítanie obrázkov
image1 = Image.open(resource_path("Fakulta_Výrobných_technológií_TUKE_logo.png"))
image1 = image1.resize((100, 100))
photo1 = ImageTk.PhotoImage(image1)

image2 = Image.open(resource_path("A_PT.png"))
image2 = image2.resize((184, 184))
photo2 = ImageTk.PhotoImage(image2)

# Zobrazenie obrázkov
background_label1 = Label(m, image=photo1)
background_label1.place(relx=0.9, rely=0.9, anchor="center")

background_label2 = Label(m, image=photo2)
background_label2.place(relx=0.5, rely=0.74, anchor="center")

# Pridanie textov
w = Label(m, text='Programovacie techniky', fg="darkorange", bg="white")
w.pack(pady=7)

w1 = Label(m, text='Lysenko Viacheslav', fg="darkorange", bg="white")
w1.pack(pady=7)

w2 = Label(m, text='Zadanie úlohy: 16', fg="darkorange", bg="white")
w2.pack(pady=7)

w3 = Label(m, text='Tlačítko na spustenie programu', fg="darkorange", bg="white")
w3.pack(pady=7)

# Textové pole na zadanie minimálnej hodnoty
entry_label_min = Label(m, text="Min:", bg="white")
entry_label_min.pack()

entry_min = Entry(m)
entry_min.pack(pady=7)
entry_min.insert(0, "0")  # Prednastavená minimálna hodnota

# Textové pole na zadanie maximálnej hodnoty
entry_label_max = Label(m, text="Max:", bg="white")
entry_label_max.pack()

entry_max = Entry(m)
entry_max.pack(pady=7)
entry_max.insert(0, "100")  # Prednastavená maximálna hodnota

# Textové pole na zadanie násobku
entry_label_multiplier = Label(m, text="(Voliteľný parameter)násobok :", bg="white")
entry_label_multiplier.pack()

entry_multiplier = Entry(m)
entry_multiplier.pack(pady=7)
entry_multiplier.insert(0, "1")  # Prednastavený násobok

# Tlačidlo na spustenie generovania
button1 = Button(m, text='Tlačidlo', width=25, fg="orange", bg="darkgreen", command=open_new_window)
button1.pack()

button2 = Button(m, text='A v MAIS', width=25, fg="green", bg="orange", command=m.quit)
button2.pack()

m.mainloop()