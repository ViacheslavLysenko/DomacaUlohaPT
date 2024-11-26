from tkinter import Tk, Label, Button, Entry, Toplevel
from PIL import Image, ImageTk
import random
import matplotlib.pyplot as plt

# Funkcia na generovanie čísel a zobrazenie výsledkov
def open_new_window():
    try:
        # Získame hodnoty z textových polí
        num_min = int(entry_min.get())  # Minimálna hodnota
        num_max = int(entry_max.get())  # Maximálna hodnota
    except ValueError:
        num_min = 0  # Prednastavená minimálna hodnota
        num_max = 100  # Prednastavená maximálna hodnota

    # Generovanie náhodných čísel
    numbers = [random.randint(num_min, num_max) for _ in range(12)]

    # Odčítanie čísel medzi sebou
    differences = [numbers[i] - numbers[i + 1] for i in range(len(numbers) - 1)]

    # Prirátanie 10 ku každému číslu
    adjusted_numbers = [num + 10 for num in numbers]

    # Vytvorenie reťazca pre zobrazenie pôvodných čísel a rozdielov
    differences_with_numbers = [f'{numbers[i]} - {numbers[i + 1]} = {differences[i]}' for i in range(len(differences))]

    # Vytvorenie nového okna pre zobrazenie výsledkov
    new_window = Toplevel(m)
    new_window.title("Výsledky")

    # Vypísanie výsledkov do nového okna
    result_label = Label(new_window, text=f'Čísla: {numbers}\nRozdiely:\n' + '\n'.join(differences_with_numbers))
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

# Načítanie prvého obrázka a zmena jeho veľkosti
image1 = Image.open("Fakulta_Výrobných_technológií_TUKE_logo.png")
image1 = image1.resize((100, 100))
photo1 = ImageTk.PhotoImage(image1)

# Načítanie druhého obrázka a zmena jeho veľkosti
image2 = Image.open("A_PT.png")  # Druhý obrázok
image2 = image2.resize((184, 184))
photo2 = ImageTk.PhotoImage(image2)

# Zobrazenie prvého obrázka
background_label1 = Label(m, image=photo1)
background_label1.place(relx=0.9, rely=0.9, anchor="center")  # Umiestnenie na stred

# Zobrazenie druhého obrázka
background_label2 = Label(m, image=photo2)
background_label2.place(relx=0.5, rely=0.74, anchor="center")  # Umiestnenie na stred

# Pridanie textu nad obrázok
w = Label(m, text='Programovacie techniky', fg="darkorange", bg="white")
w.pack(pady=10)

w1 = Label(m, text='Lysenko Viacheslav', fg="darkorange", bg="white")
w1.pack(pady=10)

w2 = Label(m, text='Zadanie úlohy: 16', fg="darkorange", bg="white")
w2.pack(pady=10)

w3 = Label(m, text='Tlačítko na spustenie programu', fg="darkorange", bg="white")
w3.pack(pady=10)

# Pridanie textového poľa na zadanie minimálnej hodnoty
entry_label_min = Label(m, text="Min:", bg="white")
entry_label_min.pack()

entry_min = Entry(m)
entry_min.pack(pady=15)
entry_min.insert(0, "0")  # Prednastavená minimálna hodnota

# Pridanie textového poľa na zadanie maximálnej hodnoty
entry_label_max = Label(m, text="Max:", bg="white")
entry_label_max.pack()

entry_max = Entry(m)
entry_max.pack(pady=15)
entry_max.insert(0, "100")  # Prednastavená maximálna hodnota

# Tlačidlo na spustenie generovania
button1 = Button(m, text='Tlačidlo', width=25, fg="orange", bg="darkgreen", command=open_new_window)
button1.pack()

button2 = Button(m, text='A v MAIS', width=25, fg="green", bg="orange", command=m.quit)
button2.pack()

m.mainloop()